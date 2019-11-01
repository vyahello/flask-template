from lib import app, render_template


@app.route("/")
@app.route("/index")
def home_page() -> None:
    return render_template("index.html")


@app.route("/details")
def details_page() -> None:
    return render_template("details.html")

