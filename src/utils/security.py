"""
Security and permission management.
"""

import logging
from typing import Dict, Any


class PermissionManager:
    """Manage permissions for dangerous operations."""

    DANGEROUS_OPERATIONS = [
        "delete_file",
        "delete_folder",
        "run_script",
        "system_shutdown",
        "system_restart",
    ]

    def __init__(self, config: Dict[str, Any]):
        """Initialize permission manager."""
        self.config = config
        self.logger = logging.getLogger(__name__)

        # Load permission rules from config
        self.rules = config.get("security", {}).get("require_confirmation", [])

    def requires_confirmation(self, operation: str) -> bool:
        """
        Check if operation requires user confirmation.

        Args:
            operation: Operation name

        Returns:
            True if confirmation required
        """
        return operation in self.rules or operation in self.DANGEROUS_OPERATIONS

    def request_confirmation(self, operation: str, details: str) -> bool:
        """
        Request user confirmation for dangerous operation.

        Args:
            operation: Operation name
            details: Operation details

        Returns:
            True if user confirms
        """
        self.logger.warning(f"Requesting confirmation for: {operation} - {details}")

        # TODO: Show confirmation dialog
        # For now, auto-deny dangerous operations
        return False
