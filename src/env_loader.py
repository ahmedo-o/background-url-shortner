import os
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
HOTKEY = os.getenv('HOTKEY')
TOAST_TITLE = os.getenv('TOAST_TITLE')
ICON_PATH = os.getenv('ICON_PATH')