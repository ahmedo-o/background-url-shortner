import keyboard
import pyperclip
from tinyurl import TinyURL
from toast import show_toast
from env_loader import CHANGE_HOTKEY_HOTKEY, HOTKEY, QUIT_HOTKEY


def shorten_link():
    content = pyperclip.paste()
    if not content:
        return

    shortner = TinyURL(content)
    short_url = shortner.shorten_url()

    try:
        if short_url['error']:
            show_toast(short_url['error']['message'])
    except:
        show_toast('Sucess! Shortened URL has been copied to your clipboard')
        pyperclip.copy(short_url['url'])


def change_hotkey():
    pass


keyboard.add_hotkey(HOTKEY, shorten_link)
keyboard.add_hotkey(CHANGE_HOTKEY_HOTKEY, change_hotkey)
keyboard.wait(QUIT_HOTKEY)

show_toast('Exiting...')
