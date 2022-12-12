from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    today = todays_date()
    return render_template("index.html", the_date = today)
    
@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/new_page")
def new_page():
    return render_template("new_page.html")
    
def todays_date():
    today = date.today()
    str_date = today.strftime("%B %d %Y")
    return "Today's date is : " + str_date
    