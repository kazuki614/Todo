from flask import request
from sqlalchemy import Column, DateTime, Integer, Text
import datetime

from models.base import Base
from models.base import session_scope


class BaseToDo(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    due_date = Column(DateTime, nullable=False, default=datetime.datetime.now())
    description = Column(Text)
    status = Column(Integer)

    @classmethod
    def create(cls, title: str, due_date: datetime.datetime) -> dict:
        todo = cls(title=title,
                   due_date=due_date,
                   description='',
                   status=0)
        with session_scope() as session:
            session.add(todo)
            new_todo = session.query(cls).order_by(cls.id.desc()).first()
        new_tod_dict = {
            'id': new_todo.id,
            'title': new_todo.title,
            'due': new_todo.due_date.strftime('%Y-%m-%d'),
            'status': new_todo.status}
        return new_tod_dict

    @classmethod
    def delete(cls, todo_id: int) -> bool:
        with session_scope() as session:
            todo = session.query(cls).filter(cls.id == todo_id).first()
            session.delete(todo)
        return True

    @classmethod
    def get(cls) -> list:
        with session_scope() as session:
            todos = session.query(cls).all()
        result = []
        for todo in todos:
            df = {
                'id': todo.id,
                'title': todo.title,
                'due': todo.due_date.strftime('%Y-%m-%d'),
                'description': todo.description,
                'status': todo.status
            }
            result.append(df)
        return result

    @classmethod
    def update(cls, todo_id: int, title: str, due_date, description: str, status: int) -> bool:
        with session_scope() as session:
            todo = session.query(cls).filter(cls.id == todo_id).first()
            todo.title = title
            todo.due_date = due_date
            todo.description = description
            todo.status = status
        return True


class Todo(BaseToDo, Base):
    __tablename__ = 'todo'
