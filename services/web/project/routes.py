from flask import Blueprint, render_template, request,redirect, url_for
from project.items.models import Category, Item

app = Blueprint('app',__name__)

@app.route('/')
def index():
    context = {}
    context['page_title'] = 'LaViolette | Acceuil'
    page = request.args.get('page',1, type=int)
    context['categories'] = Category.query.all()
    context['items'] = Item.query.order_by(Item.created_at.desc()).paginate(per_page=3, page=page)
    return render_template('app/home.html',context=context)

@app.context_processor
def base():
    categories = Category.query.all()
    return dict(categories=categories)
