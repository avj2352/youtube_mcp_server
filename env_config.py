"""
    load env variables
"""
import os
from dotenv import load_dotenv

load_dotenv()

# get app version
def _get_app_version():
    return os.environ.get("APP_VERSION") or "0.0.1"

# get app port number
def _get_app_port_number():
    return os.environ.get("APP_PORT") or 8080

# get youtube api key
def _get_youtube_api_key():
    return os.environ.get("YOUTUBE_API_KEY") or ""


YOTUBE_API_KEY = _get_youtube_api_key()
APP_VERSION = _get_app_version()
APP_PORT = _get_app_port_number()
