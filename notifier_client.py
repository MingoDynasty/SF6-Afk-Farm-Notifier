import logging

from chump import Application

from config import config

logger = logging.getLogger(__name__)

if config.pushover_enabled:
    app = Application(config.pushover_app_key)
    user = app.get_user(config.pushover_user_key)


# TODO: this will blindly fire off messages.
#  However, it is possible that messages will continue to fire on every scheduled run until the issue is resolved,
#  particularly in the case of a stuck afk farm.
#  It may be more optimal to instead make this an "emergency message", and leverage Pushover's
#  built-in retry/timeout logic. Then this script can wait until the previous message is acknowledged,
#  before sending a new (emergency) message. This helps ensure 1 message per 1 incident, instead of
#  multiple messages for each incident.
def send_message(message: str):
    if not config.pushover_enabled:
        return None
    return user.send_message(message)
