from ._utils import read_data


def get_response(path: str) -> list[dict]:
    response = read_data(path)
    return response
