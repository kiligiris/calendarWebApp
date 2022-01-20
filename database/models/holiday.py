from sqlalchemy.schema import Column
from sqlalchemy.types import Date, String
from database.setting import Base


class Holiday(Base):
    __tablename__ = "holiday"  # テーブル名を指定

    h_date = Column(Date, primary_key=True)
    h_name = Column(String(50))
    
    def __init__(self, h_date, h_name):
        self.h_date = h_date
        self.h_name = h_name
    
    def day_list(self):
        return [self.h_date.day, self.h_name]
    
    def day_dict(self):
        return {self.h_date.day : self.h_name}
    
    
