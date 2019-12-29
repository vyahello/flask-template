from src.support.data import pokemons_by_color


def test_pokemons_len_by_color() -> None:
    assert len(pokemons_by_color("black"))


def test_first_pokemons_by_color() -> None:
    assert isinstance(pokemons_by_color("black")[0], str)
