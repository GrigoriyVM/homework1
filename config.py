#!/usr/bin/env python3
"""
Configuration file for the application
"""

# Application settings
DEBUG = True
VERSION = "1.0"
APP_NAME = "Git Lab Project"

# Backup settings
BACKUP_COMPRESSION_LEVEL = 6
BACKUP_KEEP_COUNT = 5
BACKUP_DEFAULT_SOURCE = "."
BACKUP_DEFAULT_DEST = "./backup"

# Logging settings
LOG_ENABLED = True
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "app.log"

# Feature flags
ENABLE_EMAIL_NOTIFY = False
ENABLE_AUTO_CLEANUP = True
ENABLE_COMPRESSION = True

# Database settings (example)
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "myapp_db",
    "user": "app_user",
    "password": "changeme"  # В реальном проекте используй переменные окружения!
}

def get_config():
    """Return all config as dictionary"""
    return {key: value for key, value in globals().items() 
            if not key.startswith("_") and key.isupper()}

if __name__ == "__main__":
    print("Current configuration:")
    for key, value in get_config().items():
        print(f"{key} = {value}")
