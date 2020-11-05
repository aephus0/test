from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import keyboard
import string
import random
adding = False

testlist = []


engine = create_engine(
    'sqlite:////Users/wiggo/skolproject/test pyton/database.db', echo=True)
Base = declarative_base(bind=engine)


class testlager(Base):
    __tablename__ = 'lager'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40))
    price = Column(Integer)
    status = Column(Integer)

    def __init__(self, name, price, status):
        self.name = name
        self.price = price
        self.status = status


Base.metadata.create_all()

Session = sessionmaker(bind=engine)

s = Session()


def addItem():
    testlist.append(testlager(input("1: "), input("2: "), input(
        "3: ".format(testlager.name, testlager.price, testlager.status))))
    s.add_all(testlist)
    s.commit()


def removeItem():
    albin = input("enter the id of the item you wish to remove: ")
    testlager.remove(albin), albin.id
    s.commit()


def showItems():
    for item in s.query(testlager):
        print(type(item), item.id, item.name, item.price, item.status)


showItems()
removeItem()
showItems()
