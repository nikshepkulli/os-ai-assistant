"""
Voice input capture and wake word detection.
"""

import logging
from typing import Callable, Optional


class VoiceInput:
    """Handles microphone input and wake word detection."""

    def __init__(self, config: dict):
        """Initialize voice input system."""
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.is_listening = False
        self.callback: Optional[Callable] = None

    def start(self):
        """Start listening for wake word."""
        self.logger.info("Starting voice input...")
        self.is_listening = True
        # TODO: Initialize audio capture
        # TODO: Initialize wake word detection

    def stop(self):
        """Stop listening."""
        self.logger.info("Stopping voice input...")
        self.is_listening = False
        # TODO: Clean up audio resources

    def set_callback(self, callback: Callable):
        """Set callback for when wake word is detected."""
        self.callback = callback

    def capture_command(self, duration: int = 5) -> bytes:
        """Capture audio for command after wake word detected."""
        # TODO: Implement audio capture
        self.logger.info(f"Capturing command audio for {duration}s...")
        return b""
