import json
import os


CONFIG_FILE = "config.json"


# -------------------------------
# Default config values
# -------------------------------
DEFAULT_CONFIG = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": None,
        "password": None,
        "database": None
    },
    "api_keys": {
        "openai": None,
        "stripe": None
    },
    "features": {
        "email_notifications": False,
        "debug_mode": True,
        "rate_limit": 50
    }
}


# -------------------------------
# Load config file
# -------------------------------
def load_config():
    """
    Loads config.json safely.
    Creates file if missing.
    """
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


# -------------------------------
# Save config to file
# -------------------------------
def save_config(config: dict):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


# -------------------------------
# Validate required keys
# -------------------------------
def validate_config(config: dict):
    required_keys = {
        "database": ["host", "port", "username", "password", "name"],
        "api_keys": ["openai"],
        "features": ["email_notifications", "debug_mode", "rate_limit"]
    }

    missing = []

    for section, keys in required_keys.items():
        if section not in config:
            missing.append(section)
            continue

        for key in keys:
            if key not in config[section]:
                missing.append(f"{section}.{key}")

    return missing


# -------------------------------
# Safe getter using .get()
# -------------------------------
def get_config_value(config, section, key, default=None):
    return config.get(section, {}).get(key, default)


# -------------------------------
# Update config programmatically
# -------------------------------
def update_config(section, key, value):
    config = load_config()

    if section not in config:
        config[section] = {}

    config[section][key] = value

    save_config(config)
    return config

