from flask import Flask, render_template, url_for
import datetime
from get_calendar import get_calendar

app = Flask(__name__)

a_month = ["January","February","March","April","May","June","July","August","September","October","November","December"]

@app.route('/calendar')
@app.route('/calendar/<int:year>/<int:month>')
def index(**kw):
    today = datetime.date.today()

    try:
        show_date = datetime.date(kw["year"], kw["month"], 1)
    except:
        show_date = today

    calendar = get_calendar(show_date.year,show_date.month)
    return render_template(
        'index.html',
        date=show_date,
        today=today,
        a_month=a_month[show_date.month - 1],
        calendar=calendar
    )

if __name__ == "__main__":
    app.run(debug=True)