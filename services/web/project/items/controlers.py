from flask import Blueprint, render_template, request, url_for, redirect, flash
from project import db
from project.items.models import Category, Item
from sqlalchemy import exc
import logging

items = Blueprint('items',__name__)

@items.route('/<int:id>/detail')
def item_detail_view(id):
    context = {}
    context['page_title'] = "detail"
    try:
        item_id = id 
        context['item'] = Item.query.get(item_id)
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


