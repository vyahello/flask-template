from src import app, render_template
from src.system import Date


@app.route("/")
@app.route("/index")
def home_page() -> None:
    date: Date = Date("today")
    return render_template("index.html", time=f"{date.name()}'s date is {date.show()}")


@app.route("/details")
def details_page() -> None:
    return render_template("details.html")
