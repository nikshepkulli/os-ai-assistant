"""
macOS-specific automation using AppleScript and native APIs.
"""

import subprocess
from pathlib import Path
from typing import Optional, List

from .base import AutomationEngine


class MacOSAutomation(AutomationEngine):
    """macOS automation implementation."""

    def open_application(self, app_name: str) -> bool:
        """Open application using osascript."""
        try:
            script = f'tell application "{app_name}" to activate'
            subprocess.run(["osascript", "-e", script], check=True)
            self.logger.info(f"Opened {app_name}")
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to open {app_name}: {e}")
            return False

    def close_application(self, app_name: str) -> bool:
        """Close application using osascript."""
        try:
            script = f'tell application "{app_name}" to quit'
            subprocess.run(["osascript", "-e", script], check=True)
            self.logger.info(f"Closed {app_name}")
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to close {app_name}: {e}")
            return False

    def focus_application(self, app_name: str) -> bool:
        """Focus application."""
        return self.open_application(app_name)

    def create_file(self, path: str) -> bool:
        """Create file."""
        try:
            Path(path).touch()
            self.logger.info(f"Created file: {path}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create file: {e}")
            return False

    def create_folder(self, path: str) -> bool:
        """Create folder."""
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Created folder: {path}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create folder: {e}")
            return False

    def delete_file(self, path: str) -> bool:
        """Delete file (move to trash)."""
        try:
            # Use osascript to move to trash instead of permanent delete
            script = f'tell application "Finder" to delete POSIX file "{path}"'
            subprocess.run(["osascript", "-e", script], check=True)
            self.logger.info(f"Moved to trash: {path}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to delete file: {e}")
            return False

    def move_file(self, source: str, destination: str) -> bool:
        """Move file."""
        try:
            Path(source).rename(destination)
            self.logger.info(f"Moved {source} to {destination}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to move file: {e}")
            return False

    def copy_file(self, source: str, destination: str) -> bool:
        """Copy file."""
        try:
            import shutil
            shutil.copy2(source, destination)
            self.logger.info(f"Copied {source} to {destination}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to copy file: {e}")
            return False

    def list_files(self, path: str) -> List[str]:
        """List files in directory."""
        try:
            return [str(p) for p in Path(path).iterdir()]
        except Exception as e:
            self.logger.error(f"Failed to list files: {e}")
            return []

    def set_volume(self, level: int) -> bool:
        """Set volume using osascript."""
        try:
            script = f"set volume output volume {level}"
            subprocess.run(["osascript", "-e", script], check=True)
            self.logger.info(f"Set volume to {level}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to set volume: {e}")
            return False

    def set_brightness(self, level: int) -> bool:
        """Set brightness."""
        # TODO: Implement using PyObjC
        self.logger.warning("Brightness control not yet implemented")
        return False

    def take_screenshot(self, path: Optional[str] = None) -> str:
        """Take screenshot using screencapture."""
        try:
            if path is None:
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                path = str(Path.home() / f"screenshot_{timestamp}.png")

            subprocess.run(["screencapture", path], check=True)
            self.logger.info(f"Screenshot saved to {path}")
            return path
        except Exception as e:
            self.logger.error(f"Failed to take screenshot: {e}")
            return ""

    def search_web(self, query: str) -> bool:
        """Search web."""
        import webbrowser
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        return True

    def open_url(self, url: str) -> bool:
        """Open URL."""
        import webbrowser
        webbrowser.open(url)
        return True

    def get_system_info(self, info_type: str) -> str:
        """Get system info."""
        # TODO: Implement battery, wifi, etc
        return f"{info_type}: Not implemented yet"
