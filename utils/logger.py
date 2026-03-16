import logging
import os


def get_logger(name):

    log_dir = "reports/logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "test_execution.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger