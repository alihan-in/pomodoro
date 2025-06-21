from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/pomodoro')

Session = sessionmaker(engine)


def get_db_connect() -> Session:
    return Session
