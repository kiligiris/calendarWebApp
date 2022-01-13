from database.setting import engine, Base
from database.models.user import User
from database.models.holiday import Holiday
from database.models.schedule import Schedule

def main():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()