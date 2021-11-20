import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQL_ALCHEMY_DATABASE_URL = "postgresql://bbpcwcvyjazdcm:ff8df7bba28207eb19ab3f814f9dee7785b96e01fd62b2def45c8cf3ab173340@ec2-54-210-226-209.compute-1.amazonaws.com:5432/d6d55r1q43igua"
SQL_ALCHEMY_DATABASE_URL = "sqlite:///north.db"
# or other relevant config var if uri.startswith("postgres://"):     uri = uri.replace("postgres://", "postgresql://", 1)
uri = os.getenv("SQL_ALCHEMY_DATABASE_URL")

engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
