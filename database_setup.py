import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.create_all(engine)


######insert at the end of file#########
def create_all_tables():
    # create all table corresponding to the classes
    # we are using sqllite here
    engine = create_engine("sqlite:///restaurant.db")
    Base.metadata.create_all(engine)

def get_session():
    engine = create_engine('sqlite:///restaurant.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def add_restaurant(name):
    session = get_session()
    newEntry = Restaurant(name=name)
    session.add(newEntry)
    session.commit()
    session.close()

def get_all_restaurants():
    session = get_session()
    restaurants = session.query(Restaurant).all()
    session.close()
    return restaurants

def get_restaurant(id):
    session = get_session()
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    session.close()
    return restaurant

def delete_restaurants():
    session = get_session()
    session.query(Restaurant).delete()
    session.commit()
    session.close()

def delete_restaurant(rest_id):
    session = get_session()
    session.query(Restaurant).filter_by(id=rest_id).delete()
    session.commit()
    session.close()

def update_restaurantName(id, new_name):
    session = get_session()
    restaurant = get_restaurant(id)
    if restaurant != []:
        restaurant.name = new_name
        session.add(restaurant)
        session.commit()

def add_menuitem(_name, _description, _course, _price, _restaurant):
    session = get_session()
    newitem = MenuItem(name=_name, description=_description, course=_course, price=_price, restaurant= _restaurant)
    session.add(newitem)
    session.commit
    session.close()

def update_item_price(target_name, new_price):
    session = get_session()
    # find entry
    target = session.query(MenuItem).filter_by(name=target_name).one()
    # value to reset
    target.price = new_price
    # add to session
    session.add(target_name)
    # commit to session
    session.commit()
    session.close()

def delete_item(target_name):
    session = get_session()
    target = session.query(MenuItem).filter_by(name=target_name).one() #find the entry
    session.delete(target) # delete the entry
    session.commit() # commit the entry again
    session.close()