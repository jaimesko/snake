"""
This module defines the setup_logger function, which sets up a logger for the game.

The setup_logger function configures the logger to write logs to a file and 
the console, with a specific format for the log messages.
"""
import logging


def setup_logger(
    name: str,
    log_file: str,
    logger_level: int = logging.WARNING,
    console_level: int = logging.WARNING,
    file_level: int = logging.ERROR,
) -> logging.Logger:
    """Function to setup a custom logger with different levels for console and file output."""

    # Create a custom logger
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(logger_level)

    # Create a console handler
    console_handler: logging.StreamHandler = logging.StreamHandler()
    console_handler.setLevel(console_level)

    # Create a file handler
    file_handler: logging.FileHandler = logging.FileHandler(log_file)
    file_handler.setLevel(file_level)

    # Create a formatter and add it to the handlers
    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
