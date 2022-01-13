from sqlalchemy.schema import Column
from sqlalchemy.types import Date, String
from database.setting import Base


class Holiday(Base):
    __tablename__ = "holiday"  # テーブル名を指定

    h_date = Column(Date, primary_key=True)
    h_name = Column(String(50))