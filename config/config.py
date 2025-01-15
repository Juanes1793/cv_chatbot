from pathlib import Path
from dotenv import dotenv_values
import os

BASE_DIR = Path.cwd().parent
ENV_VARIABLES = {
    **dotenv_values(BASE_DIR / ".env"),
    **os.environ

}