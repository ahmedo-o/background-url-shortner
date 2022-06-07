import win10toast


from win10toast import ToastNotifier
from env_loader import TOAST_TITLE, ICON_PATH

notifier = ToastNotifier()


def show_toast(msg):
    notifier.show_toast(TOAST_TITLE, msg, ICON_PATH, threaded=True)
