import pytest

from statsbombpy_local._utils import read_env, read_data


def test_read_env() -> None:
    with pytest.raises(KeyError):
        read_env("foo")


def test_read_data() -> None:
    data = read_data("tests/data/competitions.json")
    assert data[0]["competition_id"] == 9
