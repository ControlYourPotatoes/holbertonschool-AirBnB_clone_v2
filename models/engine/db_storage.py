#!/usr/bin/python3
"""
Handles the storage when the engine depends on a MySQL database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

classes = {'State': State, 'City': City, 'User': User,
           'Place': Place, 'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """SqlAlchemy Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            
            for cls in self.classes.values():
                query = self.__session.query(cls).all()
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()