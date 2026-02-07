import pytest

from app.main import get_human_age


def test_zero_age_returns_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_15_years_returns_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_15_yers_returns_1() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_under_24_years_returns_zero() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_24_yers_returns_2() -> None:
    assert get_human_age(24, 24) == [2, 2]


testdata = [
    (0, -1),
    (-1, 0),
    (-1, -1),
]


@pytest.mark.parametrize("cat_years,dog_years", testdata)
def test_negative_age(cat_years: int, dog_years: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_years, dog_years)


testdata = [
    ({}, 5),
    ([], 2),
    ("str", -1),
    ([1, 2], -1),
    ({1, 2}, -1),
    ({"a": "1"}, -1),
]


@pytest.mark.parametrize("cat_years,dog_years", testdata)
def test_age_is_number(cat_years: object, dog_years: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)


testdata = [(27, 27, [2, 2]), (28, 28, [3, 2]), (100, 100, [21, 17])]


@pytest.mark.parametrize("cat_years,dog_years,expected", testdata)
def test_each_next_years_after_24(
    cat_years: int, dog_years: int, expected: list[int]
) -> None:
    assert get_human_age(cat_years, dog_years) == expected
