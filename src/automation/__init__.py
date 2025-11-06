"""OS Automation modules for different platforms."""

import sys
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import AutomationEngine


def get_automation_engine(config: dict) -> "AutomationEngine":
    """
    Get the appropriate automation engine for the current platform.

    Args:
        config: Application configuration

    Returns:
        Platform-specific automation engine
    """
    logger = logging.getLogger(__name__)
    platform = sys.platform

    if platform == "darwin":
        from .macos import MacOSAutomation
        logger.info("Using macOS automation engine")
        return MacOSAutomation(config)
    elif platform.startswith("linux"):
        from .linux import LinuxAutomation
        logger.info("Using Linux automation engine")
        return LinuxAutomation(config)
    elif platform == "win32":
        from .windows import WindowsAutomation
        logger.info("Using Windows automation engine")
        return WindowsAutomation(config)
    else:
        raise NotImplementedError(f"Platform {platform} not supported")
