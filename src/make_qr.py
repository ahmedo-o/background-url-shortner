import qrcode
import validators


def make_qr(url):
    if not validators.url(url):
        return False, None

    return True, qrcode.make(url)
