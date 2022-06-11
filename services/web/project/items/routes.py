from flask import Blueprint, render_template, request
from project.models import Category, Item
from sqlalchemy import exc
import logging
from sqlalchemy.orm import Query

item = Blueprint('item',__name__)

@item.route('/<string:item_name>/detail')
def item_detail_view(item_name):
    context = {}
    context['page_title'] = "detail"
    try:
        name = item_name 
        context['item'] = Item.query.filter_by(name=name).one()
    except exc.SQLAlchemyError as e:
        logging.debug(f"something wrong when retreivin item : {e}")

    return render_template('items/item_detail.html',context=context)


@item.route('/<string:category>/')
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


@item.route('/search_item', methods=['GET','POST'])
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