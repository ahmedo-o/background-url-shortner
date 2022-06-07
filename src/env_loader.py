import os
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN  = os.getenv('AUTH_TOKEN')
HOTKEY      = os.getenv('HOTKEY')
QR_HOTKEY   = os.getenv('QR_HOTKEY')
CHANGE_HOTKEY_HOTKEY = os.getenv('CHANGE_HOTKEY_HOTKEY')
QUIT_HOTKEY = os.getenv('QUIT_HOTKEY')
TOAST_TITLE = os.getenv('TOAST_TITLE')
ICON_PATH   = os.getenv('ICON_PATH')
