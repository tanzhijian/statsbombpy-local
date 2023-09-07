import warnings
from pathlib import Path

import pytest
from pandas import DataFrame
from statsbombpy.api_client import NoAuthWarning

from statsbombpy_local._api import (
    competitions,
    matches,
    lineups,
    events,
    frames,
    competition_events,
)
from statsbombpy_local._utils import generate_paths


@pytest.fixture(autouse=True)
def ignore_no_auth_warning():
    warnings.filterwarnings("ignore", category=NoAuthWarning)


base_test_path = str(Path(Path.cwd(), "tests/data/")) + "/"
LOCAL_TEST_PATHS = generate_paths(base_test_path)


def test_competitions():
    c = competitions(local_paths=LOCAL_TEST_PATHS)
    if isinstance(c, DataFrame):
        assert c.loc[0].competition_id == 9


def test_matches():
    m = matches(2, 44, local_paths=LOCAL_TEST_PATHS)
    if isinstance(m, DataFrame):
        assert m.loc[0].away_team == "Arsenal"


def test_lineups():
    lu = lineups(7298, local_paths=LOCAL_TEST_PATHS)
    assert lu["Chelsea FCW"].loc[0].jersey_number == 16


def test_events():
    e = events(7298, local_paths=LOCAL_TEST_PATHS)
    if isinstance(e, DataFrame):
        assert e.loc[0].possession_team == "Manchester City WFC"


def test_fframes():
    fm = frames(3788741, local_paths=LOCAL_TEST_PATHS)
    if isinstance(fm, DataFrame):
        assert not fm.loc[0].keeper


def test_competition_events():
    ce = competition_events(
        country="Europe",
        division="Champions League",
        season="2017/2018",
        local_paths=LOCAL_TEST_PATHS,
    )
    if isinstance(ce, DataFrame):
        assert ce.loc[0].possession_team == "Real Madrid"
