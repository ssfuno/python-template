"""Provide a logger that is configured to work with Google Cloud Logging."""

import logging
import os

IS_CLOUD_RUN_ENVIRONMENT = "K_SERVICE" in os.environ

log_level_str = os.environ.get("LOG_LEVEL", "INFO")
log_level = getattr(logging, log_level_str.upper(), logging.INFO)

if IS_CLOUD_RUN_ENVIRONMENT:
    import google.cloud.logging

    client = google.cloud.logging.Client()
    client.setup_logging(log_level=log_level)
else:
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_logger(name: str) -> logging.Logger:
    """Get a logger with the specified name.

    Args:
        name: The name of the logger.

    Returns:
        A logger instance.

    """
    return logging.getLogger(name)
