from src.support.data import get_random_joke


def test_len_random_joke() -> None:
    assert len(get_random_joke())


def test_type_random_joke() -> None:
    assert isinstance(get_random_joke(), str)
