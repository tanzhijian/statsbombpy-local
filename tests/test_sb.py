import warnings
from pathlib import Path

import pytest
from pandas import DataFrame
from statsbombpy.api_client import NoAuthWarning

from statsbombpy_local.sb import competitions
from statsbombpy_local._config import Paths


@pytest.fixture(autouse=True)
def ignore_no_auth_warning():
    warnings.filterwarnings("ignore", category=NoAuthWarning)


def test_competitions() -> None:
    path = Path(Path.cwd(), "tests/data/")
    c = competitions(local_paths=Paths(path))
    if isinstance(c, DataFrame):
        assert c.loc[0].competition_id == 9
