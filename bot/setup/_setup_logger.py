import logging
from logging import Logger


def setup_logger(logging_level: str) -> Logger:
    assert isinstance(logging_level, str), "logging_level should be a string"
    assert logging_level in [
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ], "logging_level should be one of debug, info, warning, error or critical"
    logger = logging.getLogger("HuffSTBot")
    if logging_level == "debug":
        logger.setLevel(logging.DEBUG)
    elif logging_level == "info":
        logger.setLevel(logging.INFO)
    elif logging_level == "warning":
        logger.setLevel(logging.WARNING)
    elif logging_level == "error":
        logger.setLevel(logging.ERROR)
    elif logging_level == "critical":
        logger.setLevel(logging.CRITICAL)
    else:
        raise ValueError(
            f"Logging level {logging_level} is not one of the accepted values of debug, info, warning, error or critical"
        )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
