# statsbombpy-local

statsbombpy uses local open-data.

If you have [open-data](https://github.com/statsbomb/open-data) downloaded locally, you can use it.

## Installation

```
pip install statsbombpy-local
```

## Configuration

Write open-data path to .env or add environment variable: `OPEN_DATA_REPO_PATH=your open-data repo path`


## Usage

```python
from statsbombpy_local import sb
```

Same as [statsbombpy](https://github.com/statsbomb/statsbombpy)

```python
sb.competitions()
sb.matches(competition_id=2, season_id=44)
sb.lineups(match_id=3749068)["Arsenal"]
sb.events(match_id=3749068)
sb.frames(match_id=3788741)
```

### Note

* `"competitions", "matches", "lineups", "events", "frames",` these five functions use local open-data.
* The rest uses the original functions of statsbombpy, which requires network requests.
