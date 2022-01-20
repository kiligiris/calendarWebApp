from database.setting import session
from database.models.user import User
from database.models.holiday import Holiday
from database.models.schedule import Schedule


def try_for(funcs):
    try:
        for func in funcs:
            func()
        
        session.commit()
        session.close()
        return True
    except:
        session.rollback()
        session.close()
        return False

def h_select(mi, ma):
    return session.query(Holiday).\
        filter(Holiday.h_date >= mi).\
        filter(Holiday.h_date <  ma).all()

def h_add(**kwargs):
    
    def h_add_func(d, n):
        return lambda: session.add(Holiday(d, n))
    
    funcs = [
        h_add_func(k, d)
        for k, d in kwargs.items()
        ]
    return try_for(funcs)