from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from database.setting import Base

class User(Base):
    __tablename__ = "user"  # テーブル名を指定

    user_num = Column(Integer, primary_key=True)
    userID = Column(String(50), unique=True)
    password = Column(String(50))
    guest = Column(Integer)