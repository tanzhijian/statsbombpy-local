from statsbombpy_local._public import get_response

from .test_api import LOCAL_TEST_PATHS


def test_get_response():
    response = get_response(LOCAL_TEST_PATHS["competitions"])
    assert response[0]["competition_id"] == 55
