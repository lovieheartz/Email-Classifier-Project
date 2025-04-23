# app/logger.py

import logging


def get_logger(name: str = "email_classifier") -> logging.Logger:
    """
    Returns a logger with a predefined format.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger(name)
