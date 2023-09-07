import os
import json


def read_env(name: str) -> str:
    if (value := os.getenv(name)) is None:
        raise KeyError(f"Environment variable {name} not found")
    return value


def read_data(path: str) -> list[dict]:
    with open(path) as f:
        data = json.load(f)
    return data


def generate_paths(base_path: str) -> dict[str, str]:
    return {
        "competitions": base_path + "competitions.json",
        "matches": base_path + "matches/{competition_id}/{season_id}.json",
        "lineups": base_path + "lineups/{match_id}.json",
        "events": base_path + "events/{match_id}.json",
        "frames": base_path + "three-sixty/{match_id}.json",
    }
