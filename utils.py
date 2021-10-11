from datetime import datetime
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def log(line: str) -> None:
    with open(os.path.join(BASE_DIR, 'log'), 'a+', encoding='utf8') as file:
        file.write(f"[{str(datetime.now())}] -> Error -> {str(line)}\n") 