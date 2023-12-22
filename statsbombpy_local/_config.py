from dotenv import load_dotenv

from ._utils import generate_paths, read_env

load_dotenv()


base_path = f"{read_env('OPEN_DATA_REPO_PATH')}/data/"
LOCAL_PATHS = generate_paths(base_path)
