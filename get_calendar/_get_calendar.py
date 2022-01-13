DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

_week = [
    "Sun",
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat"
]
_start_day = "Sun"
_week_len = 7

# 始まりの曜日を変更
def change_start_day(day):
    global _start_day, _week
    
    for d in _week:
        if d == day:
            _start_day = day
            # _week配列を_start_dayに合わせて変更
            idx = _week.index(_start_day)
            _week = _week[idx:] + _week[:idx]
            return True
    return False

# 指定された日付の曜日番号を返す
def get_day_num(year,month,day):
    if month <= 2 :
        year -= 1
        month += 12
    y = year % 100
    h = (day + 26 * (month + 1) // 10 + y + y // 4 - 2 * year // 100 + year // 400) % 7
    return (h + _week.index("Sat")) % _week_len
    

# 指定された月の始まりの曜日を返す
def get_first_day(year,month):
    return get_day_num(year,month,1)

# 閏年かどうか True or False
def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 指定された月の日数を返す
def get_days(year,month):
    if month == 2 and check_leap_year(year): # 二月で閏年だったら
        return DAYS[month - 1] + 1
    return DAYS[month - 1]

# 指定した年月のカレンダーをリストで返す
def get_calendar(year,month):
    days = get_days(year,month)
    fday = get_first_day(year,month)
    calendar = []
    week = [0] * fday
    for day in range(1,days + 1):
        week.append(day)
        if len(week) == _week_len:
            calendar.append(week)
            week = []
    if week:
        week += [0] * (_week_len - len(week))
        calendar.append(week)
    
    return calendar