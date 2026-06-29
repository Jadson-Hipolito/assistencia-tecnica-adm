import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Any

from jose import jwt

from .config import config


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    derived_key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
    return f"pbkdf2_sha256$100000$" + salt.hex() + "$" + derived_key.hex()


def verify_password(plain: str, hashed: str) -> bool:
    if not hashed or not hashed.startswith("pbkdf2_sha256$"):
        return False

    try:
        _, iterations, salt_hex, derived_hex = hashed.split("$", 3)
        iterations = int(iterations)
        salt = bytes.fromhex(salt_hex)
        expected_key = bytes.fromhex(derived_hex)
        actual_key = hashlib.pbkdf2_hmac("sha256", plain.encode("utf-8"), salt, iterations)
        return secrets.compare_digest(actual_key, expected_key)
    except (ValueError, TypeError):
        return False


def create_access_token(data: dict[str, Any]) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)


def decode_access_token(token: str) -> dict[str, Any]:
    return jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])