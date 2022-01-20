import requests
import datetime
from get_calendar.calendar import last_month, next_month
from database.crud import h_select, h_add

# 年月を受け取り祝日の{日付 : 名前}を返す関数
def holiday(year,month):
    mi = "{}-{}-1".format(year, month)
    ma = "{}-{}-1".format(*next_month(year,month))
    datas = h_select(mi, ma)
    ret = {}
    if datas:
        ret = {d.h_date.day : d.h_name for d in datas}
        print(ret)
    else:
        ex = h_select(f"{year}-1-1", f"{year + 1}-1-1")
        # ↓祝日情報が登録されていない and 取得成功
        if not ex and bring_up(year):
            datas = h_select(mi, ma)
            ret = {d.h_date.day : d.h_name for d in datas}
    return ret

# 祝日データを自動で取得、データベースに登録する関数
def bring_up(year):
    if year > datetime.date.today().year + 1 or year < 2015:
        return False
    url = f"https://holidays-jp.github.io/api/v1/{year}/date.json"

    response = requests.get(url)

    jsonData = response.json()
    print("requestsしました")
    return h_add(**jsonData)
