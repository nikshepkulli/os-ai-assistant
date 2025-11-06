"""
Visual overlay for displaying transcriptions and feedback.
"""

import logging


class OverlayUI:
    """On-screen overlay for visual feedback."""

    def __init__(self, config: dict):
        """Initialize overlay."""
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.visible = False

        # TODO: Initialize tkinter or PyQt window

    def show(self):
        """Show the overlay."""
        self.visible = True
        # TODO: Implement

    def hide(self):
        """Hide the overlay."""
        self.visible = False
        # TODO: Implement

    def update_text(self, text: str):
        """Update displayed text."""
        self.logger.info(f"Overlay: {text}")
        # TODO: Implement

    def show_transcription(self, text: str):
        """Show real-time transcription."""
        self.update_text(f"🎤 {text}")

    def show_action(self, action: str):
        """Show action being performed."""
        self.update_text(f"⚡ {action}")

    def show_success(self, message: str):
        """Show success message."""
        self.update_text(f"✅ {message}")

    def show_error(self, message: str):
        """Show error message."""
        self.update_text(f"❌ {message}")
