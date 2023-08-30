import warnings
from pathlib import Path

import pytest
from pandas import DataFrame
from statsbombpy.api_client import NoAuthWarning

from statsbombpy_local.sb import competitions, matches, lineups, events
from statsbombpy_local._config import Paths


@pytest.fixture(autouse=True)
def ignore_no_auth_warning():
    warnings.filterwarnings("ignore", category=NoAuthWarning)


path = Path(Path.cwd(), "tests/data")


def test_competitions() -> None:
    c = competitions(local_paths=Paths(path))
    if isinstance(c, DataFrame):
        assert c.loc[0].competition_id == 9


def test_matches() -> None:
    m = matches(2, 44, local_paths=Paths(path))
    if isinstance(m, DataFrame):
        assert m.loc[0].away_team == "Arsenal"


def test_lineups() -> None:
    lu = lineups(7298, local_paths=Paths(path))
    assert lu["Chelsea FCW"].loc[0].jersey_number == 16


def test_events() -> None:
    e = events(7298, local_paths=Paths(path))
    if isinstance(e, DataFrame):
        assert e.loc[0].possession_team == "Manchester City WFC"
