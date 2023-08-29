from pathlib import Path

from dotenv import load_dotenv

from ._utils import read_env


load_dotenv()


BASE_PATH = f"{read_env('OPEN_DATA_REPO_PATH')}/data"
BASE_URL = "https://raw.githubusercontent.com/statsbomb/open-data/master/data"


class Paths:
    def __init__(self, base_path: str | Path) -> None:
        self.base_path = str(base_path)

    def competitions(self) -> str:
        return f"{self.base_path}/competitions.json"

    def matches(self, competition_id: int, season_id: int) -> str:
        return f"{self.base_path}/matches/{competition_id}/{season_id}.json"

    def lineups(self, match_id: int) -> str:
        return f"{self.base_path}/lineups/{match_id}.json"

    def events(self, match_id: int) -> str:
        return f"{self.base_path}/events/{match_id}.json"

    def frames(self, match_id: int) -> str:
        return f"{self.base_path}/three-sixty/{match_id}.json"
