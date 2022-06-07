import win32clipboard
from io import BytesIO
from PIL.Image import Image


def copy_image_to_clipboard(image: Image):
    out = BytesIO()
    image.convert('RGB').save(out, 'BMP')
    data = out.getvalue()[14:]
    out.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
