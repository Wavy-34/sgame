from os import environ
from typing import Any
from dotenv import load_dotenv  # type: ignore

from sgame.errors import EnvVarNotFound

load_dotenv()


def unpack_env_var(key: str) -> Any:
    env_var = environ.get(key)
    if env_var is None:
        raise EnvVarNotFound(f"Couldn't locate {key} in .env")
    return env_var


NOTION_DATABASE_ID = unpack_env_var("NOTION_DATABASE_ID")
NOTION_TOKEN = unpack_env_var("NOTION_TOKEN")

DISCORD_TOKEN = unpack_env_var("DISCORD_TOKEN")

DATABASE_NAME = unpack_env_var("DATABASE_NAME")
DATABASE_PASSWORD = unpack_env_var("DATABASE_PASSWORD")
DATABASE_USER = unpack_env_var("DATABASE_USER")
