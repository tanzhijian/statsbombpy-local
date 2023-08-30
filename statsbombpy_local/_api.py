from statsbombpy import sb
from statsbombpy.api_client import has_auth
from statsbombpy.config import DEFAULT_CREDS
from requests_mock import Mocker
from pandas import DataFrame

from ._config import BASE_PATH, BASE_URL, Paths
from ._utils import read_data


_local_paths = Paths(BASE_PATH)
_remote_paths = Paths(BASE_URL)


def competitions(
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: Paths = _local_paths,
) -> DataFrame | dict:
    if has_auth(creds) is True:
        return sb.competitions(fmt, creds)

    with Mocker() as m:
        data = read_data(local_paths.competitions())
        m.get(_remote_paths.competitions(), json=data)
        sb_competitions = sb.competitions(fmt)
    return sb_competitions


def matches(
    competition_id: int,
    season_id: int,
    fmt="dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: Paths = _local_paths,
) -> DataFrame | dict:
    if has_auth(creds) is True:
        return sb.matches(competition_id, season_id, fmt, creds)

    with Mocker() as m:
        data = read_data(local_paths.matches(competition_id, season_id))
        m.get(_remote_paths.matches(competition_id, season_id), json=data)
        sb_matches = sb.matches(competition_id, season_id, fmt)
    return sb_matches


def lineups(
    match_id: int,
    fmt="dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: Paths = _local_paths,
) -> dict[str, DataFrame]:
    if has_auth(creds) is True:
        return sb.lineups(match_id, fmt, creds)

    with Mocker() as m:
        data = read_data(local_paths.lineups(match_id))
        m.get(_remote_paths.lineups(match_id), json=data)
        sb_lineups = sb.lineups(match_id, fmt)
    return sb_lineups


def events(
    match_id: int,
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    flatten_attrs: bool = True,
    creds: dict = DEFAULT_CREDS,
    include_360_metrics=False,
    local_paths: Paths = _local_paths,
) -> DataFrame | dict:
    if has_auth(creds) is True:
        return sb.events(
            match_id,
            split,
            filters,
            fmt,
            flatten_attrs,
            creds,
            include_360_metrics,
        )

    with Mocker() as m:
        data = read_data(local_paths.events(match_id))
        m.get(_remote_paths.events(match_id), json=data)
        sb_events = sb.events(
            match_id=match_id,
            split=split,
            filters=filters,
            fmt=fmt,
            flatten_attrs=flatten_attrs,
            include_360_metrics=include_360_metrics,
        )
    return sb_events


def frames(
    match_id: int,
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: Paths = _local_paths,
) -> DataFrame | list | dict:
    if has_auth(creds) is True:
        return sb.frames(match_id, fmt, creds)

    with Mocker() as m:
        data = read_data(local_paths.frames(match_id))
        m.get(_remote_paths.frames(match_id), json=data)
        sb_frames = sb.frames(match_id, fmt)
    return sb_frames


competition_events = sb.competition_events
competition_frames = sb.competition_frames
player_match_stats = sb.player_match_stats
player_season_stats = sb.player_season_stats
team_season_stats = sb.team_season_stats
