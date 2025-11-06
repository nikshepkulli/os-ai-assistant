"""
Linux automation (placeholder for future implementation).
"""

from .base import AutomationEngine


class LinuxAutomation(AutomationEngine):
    """Linux automation - to be implemented."""

    def __init__(self, config: dict):
        super().__init__(config)
        self.logger.warning("Linux automation not yet fully implemented")

    # Stub implementations - TODO: Implement all methods
    def open_application(self, app_name: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def close_application(self, app_name: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def focus_application(self, app_name: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def create_file(self, path: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def create_folder(self, path: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def delete_file(self, path: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def move_file(self, source: str, destination: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def copy_file(self, source: str, destination: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def list_files(self, path: str):
        raise NotImplementedError("Linux support coming in v0.2")

    def set_volume(self, level: int) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def set_brightness(self, level: int) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def take_screenshot(self, path=None) -> str:
        raise NotImplementedError("Linux support coming in v0.2")

    def search_web(self, query: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def open_url(self, url: str) -> bool:
        raise NotImplementedError("Linux support coming in v0.2")

    def get_system_info(self, info_type: str) -> str:
        raise NotImplementedError("Linux support coming in v0.2")
