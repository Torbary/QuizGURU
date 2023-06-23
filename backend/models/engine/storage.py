#!/usr/bin/python3
'''this module defines a class to manage storage to a database'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.quiz import Quiz
from models.answer import Answer
from models.question import Question
from models.score import Score


class Storage:
    '''
    manages storage of the app model in a database
    '''
    _instance = None

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super().__new__(self)
            self._instance.__engine = create_engine(
                'sqlite:///test_db.sqlite',
                pool_pre_ping=True
            )
            self._instance.reload()
        return self._instance

    def __init__(self):
        """
        initialize the db storage
        """

    def save(self):
        '''
        commit all current session changes
        '''
        from sqlalchemy.exc import SQLAlchemyError
        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            '''ensure the database is still in a consistent state'''
            self.__session.rollback()
            print("ERR: rolling back commit")
            print(e)

    def reload(self):
        """
        reloads the session from the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
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

    def all(self, cls):
        """
        query all model of type cls
        """
        if not issubclass(cls, BaseModel):
            """
            avoid fetching a data that's not derived from BaseModel
            """
            return None
        try:   
            models = self.__session.query(cls).all()
            return models
        except SQLAlchemyError as e:
            print(e)
            return None

    def close(self):
        '''
        close the database storage
        '''
        self.__session.close()

    def drop(self):
        """
        drops all tables in the database
        """
        Base.metadata.drop_all(bind=self.__engine)
        '''
        reloads the database, so new tables
        can be created
        '''
        self.reload()
