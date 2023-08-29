from statsbombpy_local._config import Paths, BASE_URL


def test_paths() -> None:
    paths = Paths(BASE_URL)
    assert paths.competitions() == BASE_URL + "/competitions.json"
    assert paths.matches(2, 1) == BASE_URL + "/matches/2/1.json"
    assert paths.lineups(1) == BASE_URL + "/lineups/1.json"
    assert paths.events(1) == BASE_URL + "/events/1.json"
    assert paths.frames(1) == BASE_URL + "/three-sixty/1.json"
