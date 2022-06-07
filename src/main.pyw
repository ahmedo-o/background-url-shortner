import keyboard
import pyperclip
from tinyurl import TinyURL
from make_qr import make_qr
from toast import show_toast
from image_copier import copy_image_to_clipboard
from env_loader import CHANGE_HOTKEY_HOTKEY, HOTKEY, QR_HOTKEY, QUIT_HOTKEY

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
        pyperclip.copy(short_url['url'])
        show_toast('Sucess! Shortened URL has been copied to your clipboard')


def generate_qr():
    content = pyperclip.paste()
    if not content:
        return

    is_valid, qr_image = make_qr(content)
    if not is_valid:
        show_toast('Clipboard content is not a valid URL')
        return

    copy_image_to_clipboard(qr_image)
    show_toast('QR code has been copied to your clipboard')

# will add soon
def change_hotkey():
    pass


keyboard.add_hotkey(HOTKEY, shorten_link)
keyboard.add_hotkey(QR_HOTKEY, generate_qr)
keyboard.add_hotkey(CHANGE_HOTKEY_HOTKEY, change_hotkey)
keyboard.wait(QUIT_HOTKEY)

show_toast('Exiting...')
