import requests
from typing import List


def random_joke() -> str:
    return requests.get("https://api.chucknorris.io/jokes/random").json()["value"]


def pokemons_by_color(color: str) -> List[str]:
    return [
        pokemon["name"]
        for pokemon in requests.get(f"https://pokeapi.co/api/v2/pokemon-color/{color.lower()}").json()[
            "pokemon_species"
        ]
    ]
