import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = BASE_DIR / "data" / "database.sqlite"

class Config:
    raw_database_url = os.getenv("DATABASE_URL", "sqlite:///../data/database.sqlite")
    if raw_database_url.startswith("sqlite:///"):
        sqlite_path = raw_database_url[len("sqlite:///"):]
        if not Path(sqlite_path).is_absolute():
            sqlite_path = (BASE_DIR / sqlite_path).resolve()
        DATABASE_URL = f"sqlite:///{sqlite_path}"
    else:
        DATABASE_URL = raw_database_url

    SECRET_KEY = os.getenv("SECRET_KEY", "chave-secreta-dev")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

config = Config()
