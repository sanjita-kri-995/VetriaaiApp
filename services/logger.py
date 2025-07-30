import logging
import os
from logging.handlers import RotatingFileHandler

from config import app_settings

APPLICATION_NAME = app_settings.APPLICATION_NAME
# Create a custom logger
logger = logging.getLogger(APPLICATION_NAME)
logger.setLevel(logging.DEBUG)  # Change to INFO or WARNING for production

# Create formatters and add to handlers
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(module)s.%(funcName)s - %(message)s"
)

# *************Console handler ********************************
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
#console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)


# Ensure the logs directory exists
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# *************File handler ********************************
log_file_path = os.path.join(log_dir, APPLICATION_NAME+".log")

# Rolling file handler (5 MB max, keep 10 backups)
file_handler = RotatingFileHandler(
    log_file_path, maxBytes=5 * 1024 * 1024, backupCount=10
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

