from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import setting

engine = create_engine(
    setting.DB_URL,
    connect_args={'check_same_thread': False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db() -> SessionLocal:
    """function for getting local session

    :returns: SessionLocal
    """
    db = None
    try:
        db = SessionLocal()  # create session from SQLAlchemy sessionmaker
        yield db
    except Exception as e:
        raise f"DB ERROR: {e}"
    finally:
        db.close()
