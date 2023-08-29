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
