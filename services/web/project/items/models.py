from project import db, admin
from sqlalchemy import String, Integer, ForeignKey, Column,Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .views import ItemModelView ,CategoryModelView, CityModelView

class Category(db.Model):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    items = relationship('Item', back_populates='category',cascade='all,delete')

    def __repr__(self) -> str:
        return self.name  

class City(db.Model):

    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    items = relationship('Item', back_populates='city', cascade='all,delete')

    def __repr__(self) -> str:
        return self.name

class Item(db.Model):

    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80),unique=True)
    adress = Column(String(100))
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship('City', back_populates='items')
    phone = Column(String(10))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    start_at = Column(DateTime)
    close_at = Column(DateTime)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='items')

    def __repr__(self) -> str:
        return self.name 


admin.add_view(CategoryModelView(Category, db.session))
admin.add_view(ItemModelView(Item, db.session))
admin.add_view(CityModelView(City, db.session))