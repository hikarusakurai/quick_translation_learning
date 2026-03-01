import os
GIT_ABS_PATH = os.environ.get("GIT_ABS_PATH", "/Users/sakuraihikari")
APP_ABS_PATH = os.path.join(GIT_ABS_PATH, "quick_translation_learning", "app")
INPUT_DIR_PATH = os.path.join(APP_ABS_PATH, "input")
DEFAULT_DATA_CSV_PATH =  os.path.join(INPUT_DIR_PATH, "quick_translation_data.csv")
DEFAULT_TIME_LIMIT = 5
MAX_QUESTIONS  = 50