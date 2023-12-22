import pytest

from statsbombpy_local._config import base_path
from statsbombpy_local._utils import generate_paths, read_data, read_env


def test_read_env():
    with pytest.raises(KeyError):
        read_env("foo")


def test_read_data():
    data = read_data("tests/data/competitions.json")
    assert data[0]["competition_id"] == 55


def test_generate_paths():
    paths = generate_paths(base_path)
    assert paths["competitions"] == base_path + "competitions.json"
    assert (
        paths["matches"].format(competition_id=2, season_id=1)
        == base_path + "matches/2/1.json"
    )
    assert paths["lineups"].format(match_id=1) == base_path + "lineups/1.json"
    assert paths["events"].format(match_id=1) == base_path + "events/1.json"
    assert (
        paths["frames"].format(match_id=1) == base_path + "three-sixty/1.json"
    )
