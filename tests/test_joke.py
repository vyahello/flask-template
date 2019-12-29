from src.support.data import random_joke


def test_len_random_joke() -> None:
    assert len(random_joke())


def test_type_random_joke() -> None:
    assert isinstance(random_joke(), str)
