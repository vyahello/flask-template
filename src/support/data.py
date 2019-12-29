import requests


def get_random_joke() -> str:
    return requests.get("https://api.chucknorris.io/jokes/random").json()["value"]
