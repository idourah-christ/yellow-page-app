from flask.cli import FlaskGroup 
from app import app 
from project import db 
from project.items.models import Category
from project.users.models import User 
from project.items.models import City, Category

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    category = Category(name="Restaurant")
    db.session.add(category)
    db.session.commit()

@cli.command('create_admin')
def create_admin():
    admin = User(username='admin', email='admin@gmail.com',password='admin', admin=True)
    db.session.add(admin)
    db.session.commit()

@cli.command('cities_db')
def cities_db():
    cities = ['Brazzaville','Pointe-Noire','Dolisie']
    for city in cities:
        c = City(name=city)
        db.session.add(c)
    db.session.commit()

@cli.command('category_db')
def category_db():
    categories = ['Restaurant','Boutique','Hotel','Bar','Boite de Nuit','Marché']
    for cat in categories:
        c = Category(name=cat)
        db.session.add(c)
    db.session.commit()
    
if __name__ == "__main__":
    cli()