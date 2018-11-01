from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, quantity, color, brand, price):
    product_object = Product(
    	name=name,
        quantity=quantity,
        color=color,
        brand=brand,
        price=price)
    session.add(product_object)
    session.commit()


add_product("fountain", 5, "red", "idk", 400)

#def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)


def delete_product(id):
  session.query(Product).filter_by(
       id=id).delete()
session.commit()


delete_product(2)


def get_product(id):
  pass
