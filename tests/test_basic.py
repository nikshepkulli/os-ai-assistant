"""
Basic tests for OS AI Assistant.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_import_core_modules():
    """Test that core modules can be imported."""
    from src.core import orchestrator, voice_input, stt, nlu, tts

    assert orchestrator is not None
    assert voice_input is not None
    assert stt is not None
    assert nlu is not None
    assert tts is not None


def test_import_automation_modules():
    """Test that automation modules can be imported."""
    from src.automation import base, macos, linux, windows

    assert base is not None
    assert macos is not None
    assert linux is not None
    assert windows is not None


def test_import_ui_modules():
    """Test that UI modules can be imported."""
    from src.ui import overlay, tray

    assert overlay is not None
    assert tray is not None


def test_import_utils_modules():
    """Test that utility modules can be imported."""
    from src.utils import config, logger, security

    assert config is not None
    assert logger is not None
    assert security is not None


def test_config_loading():
    """Test configuration loading."""
    from src.utils.config import load_config

    config = load_config()
    assert isinstance(config, dict)


def test_intent_list():
    """Test that NLU has correct intents defined."""
    from src.core.nlu import NaturalLanguageUnderstanding

    assert len(NaturalLanguageUnderstanding.INTENTS) == 20
    assert "open_application" in NaturalLanguageUnderstanding.INTENTS
    assert "help_command" in NaturalLanguageUnderstanding.INTENTS
