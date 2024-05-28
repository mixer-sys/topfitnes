import logging
import secrets
import string
import sys


def get_random_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    return password


def start_logging() -> logging.Logger:
    """Start logging."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s  [%(levelname)s]  %(message)s',
    )
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)
    return logger
