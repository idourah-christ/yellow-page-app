from flask.cli import FlaskGroup 
from app import app 
from project import db 
from project.models import Category

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

if __name__ == "__main__":
    cli()