from project import db, flask_admin
from sqlalchemy import String, Integer, ForeignKey, Column,Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_admin.contrib.sqla import ModelView



class Category(db.Model):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    items = relationship('Item', back_populates='category',cascade='all,delete')

    def __repr__(self) -> str:
        return self.name  

class Item(db.Model):

    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    adress = Column(String(100))
    city = Column(String(100))
    phone = Column(String(10))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    start_at = Column(DateTime)
    close_at = Column(DateTime)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='items')

    def __repr__(self) -> str:
        return self.name 

