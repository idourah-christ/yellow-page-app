from flask.cli import FlaskGroup 
from app import app 
from project import db 
from project.items.models import Category
from project.users.models import User 

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

if __name__ == "__main__":
    cli()