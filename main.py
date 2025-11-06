#!/usr/bin/env python3
"""
OS AI Assistant - Main Entry Point

Voice-controlled OS automation across Windows, macOS, and Linux.
"""

import sys
import logging
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.core.orchestrator import Orchestrator
from src.utils.logger import setup_logging
from src.utils.config import load_config


def main():
    """Main entry point for OS AI Assistant."""
    # Set up logging
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Starting OS AI Assistant...")

    try:
        # Load configuration
        config = load_config()

        # Create and run orchestrator
        orchestrator = Orchestrator(config)
        orchestrator.run()

    except KeyboardInterrupt:
        logger.info("Shutting down gracefully...")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
