from lib import app, render_template


@app.route("/")
@app.route("/index")
def home_page() -> None:
    return render_template("index.html")

