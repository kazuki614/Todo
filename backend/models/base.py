from contextlib import contextmanager
import threading

from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import datetime

import settings

Base = declarative_base()
engine = create_engine(f'sqlite:///{settings.db_name}')
Session = scoped_session(sessionmaker(bind=engine))
lock = threading.Lock()


@contextmanager
def session_scope():
    session = Session()
    session.expire_on_commit = False
    try:
        lock.acquire()
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.expire_on_commit = True
        lock.release()


class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    due_date = Column(DateTime, nullable=False, default=datetime.datetime.now().time())
    status = Column(Integer)

    @classmethod
    def create(cls, title, due_date, status):
        todo = cls(title=title,
                   due_date=due_date,
                   status=status)
        with session_scope() as session:
            session.add(todo)

        return True

    @classmethod
    def delete(cls, id):
        session = Session()
        todo = session.query(cls).filter(cls.id == id).first()
        with session_scope() as session:
            session.delete(todo)
        return True

    @classmethod
    def get_todos_doing(cls):
        with session_scope() as session:
            todos_doing = session.query(cls).filter(cls.status == 0).all()
        result = []
        for todo in todos_doing:
            df = {
                'id': todo.id,
                'title': todo.title,
                'due': todo.due_date,
                'status': todo.status}
            result.append(df)
        return result

    @classmethod
    def get_todos_done(cls):
        with session_scope() as session:
            todos_done = session.query(cls).filter(cls.status == 1).all()
        result = []
        for todo in todos_done:
            df = {
                'id': todo.id,
                'title': todo.title,
                'due': todo.due_date,
                'status': todo.status}
            result.append(df)
        return result

    @classmethod
    def complete(cls, id):
        with session_scope() as session:
            todo = session.query(cls).filter(cls.id == id).first()
            todo.status = 1
        return True

    @classmethod
    def update(cls, id, title, due, status):
        with session_scope() as session:
            todo = session.query(cls).filter(cls.id == id).first()
            todo.title = title
            todo.due = due
            todo.status = status
        return True

    # for develop
    @classmethod
    def to_all_doing(cls):
        with session_scope() as session:
            todos = session.query(cls).all()
            for todo in todos:
                todo.status = 0
        return True


def init_db():
    Base.metadata.create_all(bind=engine)
