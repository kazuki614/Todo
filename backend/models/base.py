from contextlib import contextmanager
import threading
import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


import settings

Base = declarative_base()
engine = create_engine(f'sqlite:///{settings.db_name}')
Session = scoped_session(sessionmaker(bind=engine))
logger = logging.getLogger(__name__)
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
        logger.error(f'action=session_scope err={e}')
        session.rollback()
    finally:
        session.expire_on_commit = True
        lock.release()


def init_db():
    import models.todos
    Base.metadata.create_all(bind=engine)
