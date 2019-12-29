import pytest
from datetime import date as date_
from src.system import Date


@pytest.fixture(scope="module")
def date() -> Date:
    return Date("today")


def test_date_show(date: Date) -> None:
    assert date.show() == str(date_.today())


def test_date_name(date: Date) -> None:
    assert date.name() == "today"

