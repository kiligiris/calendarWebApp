import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

engine = create_engine("{}://{}:{}@{}:{}/{}?charset={}".format(
    os.environ["DIALECT"],
    os.environ['USER'],
    os.environ['PASSWORD'],
    os.environ['HOST'],
    os.environ["PORT"],
    os.environ['DATABASE'],
    os.environ["CHARSET"]
), echo=True)

Base = declarative_base()

session = scoped_session(
    sessionmaker(engine)
)
