"""
System tray icon and menu.
"""

import logging


class TrayIcon:
    """System tray icon for OS AI Assistant."""

    def __init__(self, config: dict):
        """Initialize system tray icon."""
        self.config = config
        self.logger = logging.getLogger(__name__)

        # TODO: Initialize pystray icon

    def show(self):
        """Show system tray icon."""
        # TODO: Implement
        pass

    def hide(self):
        """Hide system tray icon."""
        # TODO: Implement
        pass

    def set_state(self, state: str):
        """
        Set icon state.

        Args:
            state: One of "idle", "listening", "processing", "error"
        """
        self.logger.info(f"Tray icon state: {state}")
        # TODO: Update icon based on state

    def on_quit(self):
        """Handle quit menu item."""
        # TODO: Implement
        pass

    def on_settings(self):
        """Handle settings menu item."""
        # TODO: Implement
        pass
