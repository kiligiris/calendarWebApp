from flask import Flask, render_template, url_for
import datetime
from get_calendar.calendar import last_month, next_month, get_calendar
from get_calendar.get_holiday import holiday

app = Flask(__name__)

@app.route('/calendar')
@app.route('/calendar/<int:year>/<int:month>')
def index(**kw):
    today = datetime.date.today()

    try:
        show_date = datetime.date(kw["year"], kw["month"], 1)
    except:
        show_date = today
        
    y = show_date.year
    m = show_date.month

    last_url = "{}/{}/{}".format(url_for('index'),*last_month(y,m))
    next_url = "{}/{}/{}".format(url_for('index'),*next_month(y,m))
    
    return render_template(
        'index.html',
        date=show_date,
        today=today,
        calendar=get_calendar(y,m),
        holiday=holiday(y,m),
        last_url=last_url,
        next_url=next_url
    )

if __name__ == "__main__":
    app.run(debug=True)