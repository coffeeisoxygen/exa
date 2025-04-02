import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    """
    Sets up the logger for the application.
    Logs will be written to a file with rotation.
    """
    # Create a logger
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    # Create a file handler with rotation
    handler = RotatingFileHandler(
        "app.log", maxBytes=5 * 1024 * 1024, backupCount=3
    )  # 5 MB per file, 3 backups
    handler.setLevel(logging.INFO)

    # Create a logging format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # Optional: Add a console handler for debugging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


# Initialize the logger
logger = setup_logger()

# Example usage
if __name__ == "__main__":
    logger.info("Logging module initialized.")
    logger.error("This is an error message.")
