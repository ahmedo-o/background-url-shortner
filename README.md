# background-url-shortner
An easy to use url shortner that runs in the background and uses TinyURL API (as default) and other services.

# How to use

# 1. configure .env

```env
AUTH_TOKEN = '' # Your tinyurl auth token
HOTKEY = '' # Key combination to shorten the URL in your clipboard, example: space+alt+s
QR_HOTKEY = '' # Key combination to convert the URL in your clipboard to a QR code, example: space+alt+q
CHANGE_HOTKEY_HOTKEY = '' # No need to set it for now
QUIT_HOTKEY = '' # Key combination to exit, example: space+alt+esc
TOAST_TITLE = '' # A title for the toast notification
ICON_PATH = '' # A .ico file for the toast notification icon, example: ./assets/icon.ico
```

# 2. run
```
python src/main.pyw
```
