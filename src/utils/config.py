"""
Configuration management.
"""

import os
import logging
from pathlib import Path
from typing import Dict, Any
import yaml


def load_config() -> Dict[str, Any]:
    """
    Load configuration from files.

    Loads default config and merges with user config if present.
    """
    logger = logging.getLogger(__name__)

    # Default config path
    config_dir = Path(__file__).parent.parent.parent / "config"
    default_config_path = config_dir / "default_config.yaml"
    user_config_path = config_dir / "config.yaml"

    # Load default config
    if default_config_path.exists():
        with open(default_config_path) as f:
            config = yaml.safe_load(f) or {}
        logger.info("Loaded default configuration")
    else:
        logger.warning("Default config not found, using empty config")
        config = {}

    # Merge with user config if exists
    if user_config_path.exists():
        with open(user_config_path) as f:
            user_config = yaml.safe_load(f) or {}
        config.update(user_config)
        logger.info("Merged user configuration")

    # Override with environment variables
    if "OPENAI_API_KEY" in os.environ:
        config.setdefault("nlu", {})["api_key"] = os.environ["OPENAI_API_KEY"]

    return config


def save_config(config: Dict[str, Any]):
    """Save user configuration."""
    config_dir = Path(__file__).parent.parent.parent / "config"
    user_config_path = config_dir / "config.yaml"

    with open(user_config_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False)
