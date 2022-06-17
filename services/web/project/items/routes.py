from flask import Blueprint, render_template, request, url_for, redirect, flash
from project import db
from project.items.models import Category, Item
from sqlalchemy import exc
import logging
from project.items import forms as item_forms

items = Blueprint('items',__name__)

@items.route('/<string:item_name>/detail')
def item_detail_view(item_name):
    context = {}
    context['page_title'] = "detail"
    try:
        name = item_name 
        context['item'] = Item.query.filter_by(name=name).one()
    except exc.SQLAlchemyError as e:
        logging.debug(f"something wrong when retreivin item : {e}")

    return render_template('items/item_detail.html',context=context)

@items.route('/<string:category>/')
def item_by_category_view(category):
    context = {}
    context['page_title'] = 'Page Jaune | Categories'
    page = request.args.get('page', 1, type=int)
    try:
        context['categories'] = Category.query.all()
        category = Category.query.filter_by(name=category).first()
        context['items'] = Item.query.order_by(Item.created_at.desc())\
            .filter(Item.category_id==category.id).paginate(per_page=3, page=page)
       
    except exc.SQLAlchemyError as e:
        logging.debug(e)
    return render_template('items/item_by_category.html',context=context)

@items.route('/search_item', methods=['GET','POST'])
def search_item():
    context = {}
    if request.method == 'POST':
        term = request.form.get('q')
        context['page_title'] = f"result | {term}"
        page = request.args.get('page', 1, type=int)
        try:
            context['items'] = Item.query.order_by(Item.created_at.desc())\
                .filter(Item.name.like('%'+ term +'%')).paginate(per_page=3, page=page)

        except exc.NoResultFound as e:
            logging.debug(e)

    context['page_title'] = f"search"
    context['categories'] = Category.query.all()
    return render_template('items/item_result.html', context=context)

@items.route('/items', methods=['GET','POST'])
def item_list():
    context = {}
    context['page_title'] = 'Items list'
    context['items'] = Item.query.all()
    return render_template('items/item_list.html', context=context)

@items.route('/add_item', methods=['GET','POST'])
def add_item():
    context={}
    form = item_forms.AddItemForm()
    form.category.choices = categories = Category.query.all()
    if form.validate_on_submit():
        if form.city.data != 'None':
            name = form.name.data
            adress = form.adress.data 
            city = form.city.data 
            phone = form.phone.data 
            desc = form.description.data 
            category = form.category.data
            try:
                category_object = Category.query.filter(Category.name==category).one()
                item = Item(name=name, adress=adress, city=city,
                       phone=phone,description=desc,category_id=category_object.id
                )
                db.session.add(item)
                db.session.commit()
                flash('item added successfully','success')
                return redirect(url_for('items.item_list'))
            except exc.SQLAlchemyError as e:
                logging.debug(f'something went wrong when adding new item: {e}','danger')

        else:
            flash('Choose a city please','danger')

    context['page_title'] = 'add item'
    return render_template('items/add_item.html',context=context, form=form)