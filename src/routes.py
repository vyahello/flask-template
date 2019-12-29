from typing import List
from src import app, render_template, request
from src.support.data import random_joke, pokemons_by_color
from src.support.system import Date


@app.route("/")
@app.route("/index")
def home_page() -> None:
    # curl -X GET http://0.0.0.0:4000/
    date: Date = Date("today")
    # here 'time' variable goes to jinja template
    return render_template("index.html", time=f"{date.name()}'s date is {date.show()}")


@app.route("/details")
def details_page() -> None:
    # curl -X GET http://0.0.0.0:4000/details
    return render_template("details.html")


@app.route("/joke")
def joke() -> None:
    # curl -X GET http://0.0.0.0:4000/joke
    #
    # here 'joke' variable goes to jinja template
    return render_template("joke.html", joke=random_joke())


@app.route("/pokemon", methods=("GET", "POST"))
def pokemons() -> None:
    # curl -X GET http://0.0.0.0:4000/pokemon - empty pokemon list
    # curl -X POST http://0.0.0.0:4000/pokemon - empty pokemon list
    # curl -X POST -d 'pokecolor=black' http://0.0.0.0:4000/pokemon - filled pokemon list
    pokemons: List[str] = list()
    if request.method == "POST" and "pokecolor" in request.form:
        pokemons = pokemons_by_color(request.form.get("pokecolor"))
    return render_template("pokemon.html", pokemons=pokemons)
