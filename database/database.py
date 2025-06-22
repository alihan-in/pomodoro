from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings

setting = Settings()

engine = create_engine(setting.db_url)

Session = sessionmaker(engine)


def get_db_connect() -> Session:
    return Session
