"""
Manages the config file for the app, and shares that data to all other modules.
"""

import tomllib

from pydantic.dataclasses import dataclass

CONFIG_FILE = "config.toml"


@dataclass()
class ConfigData:
    """Dataclass models configuration for this app."""

    user_code: int
    polling_interval: int
    battle_count_timeout: int
    buckler_id: str
    buckler_r_id: str
    buckler_praise_date: int
    pushover_app_key: str
    pushover_user_key: str


def load_config() -> ConfigData:
    """Loads the config file for this app."""
    with open(CONFIG_FILE, "rb") as _file:
        config_dict = tomllib.load(_file)
    return ConfigData(**config_dict)


config = load_config()
