import logging

from chump import Application

from config import config

logger = logging.getLogger(__name__)

app = Application(config.pushover_app_key)
user = app.get_user(config.pushover_user_key)


def send_message(message: str):
    logger.info("Sending message: %s", message)
    return user.send_message(message)
