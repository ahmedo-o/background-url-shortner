import keyboard
import pyperclip
from env_loader import HOTKEY, TOAST_TITLE, ICON_PATH
from tinyurl import TinyURL
from win10toast import ToastNotifier

notifier = ToastNotifier()


def shorten_link():
    content = pyperclip.paste()
    if not content:
        return

    shortner = TinyURL(content)
    short_url = shortner.shorten_url()

    try:
        if short_url['error']:
            notifier.show_toast(
                TOAST_TITLE, short_url['error']['message'], ICON_PATH, 5)
    except:
        notifier.show_toast(
            TOAST_TITLE, 'Sucess! Shortened URL has been copied to your clipboard', ICON_PATH, 5)
        pyperclip.copy(short_url['url'])


keyboard.add_hotkey(HOTKEY, shorten_link)
keyboard.wait()
