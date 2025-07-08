# config.py

import os

# Base project directory
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Paths
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_ZIP = os.path.join(DATA_DIR, "GiveMeSomeCredit.zip")
TRAIN_FILE = os.path.join(DATA_DIR, "cs-training.csv")
TEST_FILE = os.path.join(DATA_DIR, "cs-test.csv")

# Kaggle config dir (if kaggle.json is stored locally in the project)
KAGGLE_CONFIG_DIR = PROJECT_ROOT
