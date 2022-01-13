from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime
from database.setting import Base

class Schedule(Base):
    __tablename__ = "schedule"  # テーブル名を指定

    user_num = Column(Integer, ForeignKey('user.user_num'), primary_key=True)
    s_num = Column(Integer, primary_key=True)
    s_datetime = Column(DateTime)
    s_name = Column(String(50))
    s_remarks = Column(String(256))