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
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(file_level)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
