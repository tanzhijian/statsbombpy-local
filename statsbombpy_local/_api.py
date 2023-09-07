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
    return sb.competitions(fmt)


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


competition_events = sb.competition_events
competition_frames = sb.competition_frames
player_match_stats = sb.player_match_stats
player_season_stats = sb.player_season_stats
team_season_stats = sb.team_season_stats
