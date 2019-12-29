from src import app, render_template
from src.support.data import get_random_joke
from src.support.system import Date


@app.route("/")
@app.route("/index")
def home_page() -> None:
    date: Date = Date("today")
    return render_template("index.html", time=f"{date.name()}'s date is {date.show()}")


@app.route("/details")
def details_page() -> None:
    return render_template("details.html")


@app.route("/joke")
def random_joke() -> None:
    return render_template("joke.html", joke=get_random_joke())
