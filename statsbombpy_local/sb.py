from statsbombpy import sb
from statsbombpy.api_client import has_auth
from statsbombpy.config import DEFAULT_CREDS
from requests_mock import Mocker
from pandas import DataFrame

from ._config import BASE_PATH, BASE_URL, Paths
from ._utils import read_data


def competitions(
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    local_paths: Paths = Paths(BASE_PATH),
    remote_paths: Paths = Paths(BASE_URL),
) -> DataFrame | dict:
    if has_auth(creds) is True:
        return sb.competitions(fmt, creds)

    with Mocker() as m:
        data = read_data(local_paths.competitions())
        m.get(remote_paths.competitions(), json=data)
        competitions = sb.competitions()
    return competitions
