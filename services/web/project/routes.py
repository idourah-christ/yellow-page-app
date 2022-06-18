from flask import Blueprint, render_template, request,redirect, url_for, flash
from project.items.models import Category, Item
from project import db 
from sqlalchemy import exc 
import logging 

app = Blueprint('app',__name__)

@app.route('/acceuil')
def home():
    context = {}
    context['page_title'] = 'LaViolette | Acceuil'
    page = request.args.get('page',1, type=int)
    context['categories'] = Category.query.all()
    context['items'] = Item.query.order_by(Item.created_at.desc()).paginate(per_page=3, page=page)
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

@app.context_processor
def base():
    categories = Category.query.all()
    return dict(categories=categories)
