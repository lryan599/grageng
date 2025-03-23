import logging
import os
from pathlib import Path
from typing import Any

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "app.log")
LOG_DIR = os.getenv("LOG_DIR", "logs")

parent_dir = Path(__file__).resolve().parents[2]
LOG_DIR = parent_dir / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s %(levelprefix)s PID: %(process)d %(message)s",
            "use_colors": True,
        },
        "default_without_colors": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s %(levelprefix)s PID: %(process)d %(message)s",
            "use_colors": False,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
        },
        "access_without_colors": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
            "use_colors": False,
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "default_file": {
            "formatter": "default_without_colors",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(LOG_DIR, LOG_FILE),
            "when": "D",
            "interval": 1,
            "backupCount": 7,
        },
        "access_file": {
            "formatter": "access_without_colors",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(LOG_DIR, LOG_FILE),
            "when": "D",
            "interval": 1,
            "backupCount": 7,
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["default", "default_file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "uvicorn.error": {"level": LOG_LEVEL},
        "uvicorn.access": {
            "handlers": ["access", "access_file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "grageng": {
            "handlers": ["default", "default_file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}


def setup_logger():
    logging.config.dictConfig(LOGGING_CONFIG)
