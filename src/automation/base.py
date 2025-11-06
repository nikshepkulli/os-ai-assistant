"""
Base automation interface for OS control.
"""

import logging
from abc import ABC, abstractmethod
from typing import Optional, List


class AutomationEngine(ABC):
    """Abstract base class for OS automation."""

    def __init__(self, config: dict):
        """Initialize automation engine."""
        self.config = config
        self.logger = logging.getLogger(__name__)

    # Application Control
    @abstractmethod
    def open_application(self, app_name: str) -> bool:
        """Open/launch an application."""
        pass

    @abstractmethod
    def close_application(self, app_name: str) -> bool:
        """Close/quit an application."""
        pass

    @abstractmethod
    def focus_application(self, app_name: str) -> bool:
        """Bring application to foreground."""
        pass

    # File Operations
    @abstractmethod
    def create_file(self, path: str) -> bool:
        """Create a new file."""
        pass

    @abstractmethod
    def create_folder(self, path: str) -> bool:
        """Create a new folder/directory."""
        pass

    @abstractmethod
    def delete_file(self, path: str) -> bool:
        """Delete a file (move to trash)."""
        pass

    @abstractmethod
    def move_file(self, source: str, destination: str) -> bool:
        """Move a file or folder."""
        pass

    @abstractmethod
    def copy_file(self, source: str, destination: str) -> bool:
        """Copy a file or folder."""
        pass

    @abstractmethod
    def list_files(self, path: str) -> List[str]:
        """List files in a directory."""
        pass

    # System Controls
    @abstractmethod
    def set_volume(self, level: int) -> bool:
        """Set system volume (0-100)."""
        pass

    @abstractmethod
    def set_brightness(self, level: int) -> bool:
        """Set screen brightness (0-100)."""
        pass

    @abstractmethod
    def take_screenshot(self, path: Optional[str] = None) -> str:
        """Take a screenshot and return path."""
        pass

    # Web/Browser
    @abstractmethod
    def search_web(self, query: str) -> bool:
        """Perform web search in default browser."""
        pass

    @abstractmethod
    def open_url(self, url: str) -> bool:
        """Open URL in default browser."""
        pass

    # System Info
    @abstractmethod
    def get_system_info(self, info_type: str) -> str:
        """Get system information (battery, wifi, etc)."""
        pass
