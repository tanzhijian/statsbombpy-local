import sys
from functools import partial

from statsbombpy import sb, public
from statsbombpy.api_client import has_auth
from statsbombpy.config import DEFAULT_CREDS
from pandas import DataFrame

from ._config import LOCAL_PATHS
from ._public import get_response


def competitions(
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: dict = LOCAL_PATHS,
) -> DataFrame | dict:
    if not has_auth(creds):
        # monkey patch
        public.get_response = get_response
        public.OPEN_DATA_PATHS = local_paths
    return sb.competitions(fmt, creds)


def matches(
    competition_id: int,
    season_id: int,
    fmt="dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: dict = LOCAL_PATHS,
) -> DataFrame | dict:
    if not has_auth(creds):
        public.get_response = get_response
        public.OPEN_DATA_PATHS = local_paths
    return sb.matches(competition_id, season_id, fmt, creds)


def lineups(
    match_id: int,
    fmt="dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: dict = LOCAL_PATHS,
) -> dict[str, DataFrame]:
    if not has_auth(creds):
        public.get_response = get_response
        public.OPEN_DATA_PATHS = local_paths
    return sb.lineups(match_id, fmt, creds)


def events(
    match_id: int,
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    flatten_attrs: bool = True,
    creds: dict = DEFAULT_CREDS,
    include_360_metrics=False,
    local_paths: dict = LOCAL_PATHS,
) -> DataFrame | dict:
    if not has_auth(creds):
        public.get_response = get_response
        public.OPEN_DATA_PATHS = local_paths
    return sb.events(
        match_id,
        split,
        filters,
        fmt,
        flatten_attrs,
        creds,
        include_360_metrics,
    )


def frames(
    match_id: int,
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: dict = LOCAL_PATHS,
) -> DataFrame | list | dict:
    if not has_auth(creds):
        public.get_response = get_response
        public.OPEN_DATA_PATHS = local_paths
    return sb.frames(match_id, fmt, creds)


def competition_events(
    country: str,
    division: str,
    season: str,
    gender: str = "male",
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    include_360_metrics=False,
    local_paths: dict = LOCAL_PATHS,
) -> DataFrame | dict:
    if not has_auth(creds):
        public.get_response = get_response
        public.OPEN_DATA_PATHS = local_paths
        # 暂时这样通过判断平台避免非 macOS 递归错误
        # 暂时不明白原因
        if sys.platform == "darwin":
            sb.events = partial(events, local_paths=local_paths)
    return sb.competition_events(
        country,
        division,
        season,
        gender,
        split,
        filters,
        fmt,
        creds,
        include_360_metrics,
    )


def competition_frames(
    country: str,
    division: str,
    season: str,
    gender: str = "male",
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: dict = LOCAL_PATHS,
) -> DataFrame | dict:
    if not has_auth(creds):
        public.get_response = get_response
        public.OPEN_DATA_PATHS = local_paths
        if sys.platform == "darwin":
            sb.frames = partial(frames, local_paths=local_paths)
    return sb.competition_frames(country, division, season, gender, fmt, creds)


player_match_stats = sb.player_match_stats
player_season_stats = sb.player_season_stats
team_season_stats = sb.team_season_stats
