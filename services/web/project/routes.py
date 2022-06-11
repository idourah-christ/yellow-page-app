from flask import Blueprint, render_template, request,redirect, url_for, flash
from config import dev
from project.models import Category, Item
from project import db 
from sqlalchemy import exc 
import logging 

from .forms import AddItemForm

app = Blueprint('app',__name__)

@app.route('/acceuil')
def home():
    context = {}
    context['page_title'] = 'Page Jaune| Acceuil'
    page = request.args.get('page',1, type=int)
    context['categories'] = Category.query.all()
    context['items'] = Item.query.order_by(Item.created_at.desc()).paginate(per_page=dev.ITEM_PER_PAGE, page=page)
    return render_template('app/home.html',context=context)

@app.route('/')
def index():
    context = {}
    context['page_title'] = "categories"
    context['categories'] = Category.query.all()
    return render_template('category_list.html', context=context)

@app.route('/categories',methods=['POST',"GET"])
def add_category():
    context = {}
    if request.method == 'POST':
        name = request.form.get('name')

        cat = Category(name=name)
        try:
            db.session.add(cat)
            db.session.commit()
            return redirect(url_for('app.index'))
        except exc.SQLAlchemyError as e:
            logging.debug("something is wrong : {}".format(e))
    context['page_title'] = 'new category'
    return render_template('category_add.html',context=context)

@app.route('/add_item', methods=['GET','POST'])
def add_item():
    context={}
    form = AddItemForm()
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
                return redirect(url_for('app.item_list'))
            except exc.SQLAlchemyError as e:
                logging.debug(f'something went wrong when adding new item: {e}','danger')

        else:
            flash('Choose a city please','danger')

    context['page_title'] = 'add item'
    return render_template('add_item.html',context=context, form=form)

@app.route('/items', methods=['GET','POST'])
def item_list():
    context = {}
    context['page_title'] = 'Items list'
    context['items'] = Item.query.all()
    return render_template('item_list.html', context=context)

@app.context_processor
def base():
    categories = Category.query.all()
    return dict(categories=categories)
