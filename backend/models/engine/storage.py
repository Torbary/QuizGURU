#!/usr/bin/python3
'''this module defines a class to manage storage to a database'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base, BaseModel
import os


class Storage:
    '''
    manages storage of the app model in a database
    '''
    _instance = None
    __engine = None
    __session = None

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super().__new__(self, *args, **kwargs)
        return self._instance

    def __init__(self):
        """
        initialize the db storage
        """
        self.__engine = create_engine(
            'sqlite:///test_db.sqlite',
            pool_pre_ping=True
        )
        self.reload()

    def save(self):
        '''
        commit all current session changes
        '''
        from sqlalchemy.exc import SQLAlchemyError
        try:
            self.__session.commit()
        except SQLAlchemyError:
            '''ensure the database is still in a consistent state'''
            self.__session.rollback()
            print("ERR: rolling back commit")
            pass

    def reload(self):
        """
        reloads the session from the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)

    def new(self, object):
        """
        create a new object
        """
        if object is not None:
            self.__session.add(object)

    def delete(self, object):
        """
        remove an object from the db session
        """
        if object is not None:
            self.__session.delete(object)

    def close(self):
        '''
        close the database storage
        '''
        self.__session.remove()
