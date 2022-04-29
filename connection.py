from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine('sqlite:///./tg.db')

Base = declarative_base()

session_maker = sessionmaker(bind=engine)


@contextmanager
def current_session():
    session = session_maker
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()