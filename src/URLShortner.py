import uuid
import requests
import pyperclip
import validators
from env_loader import AUTH_TOKEN


class URLShortner:
    def __init__(self):
        return

    def shorten_url(self, url):
        r = {}
        if not validators.url(url):
            r['error'] = {
                'message': 'Clipboard content is not a valid url'
            }

            return r

        payload = {
            'url': url,
            'domain': 'tinyurl.com',
            'alias': self.__make_alias()
        }

        response = requests.post(
            f'https://api.tinyurl.com/create?api_token={AUTH_TOKEN}', data=payload)

        if not response.ok:
            if response.status_code == 401:
                r['error'] = {
                    'message': 'Unauthorized'
                }
            elif response.status_code == 422:
                r['error'] = {
                    'message': 'Invalid URL'
                }
            elif response.status_code >= 500:
                r['error'] = {
                    'message': 'Server error'
                }
            return r

        r['url'] = response.json()['data']['tiny_url']

        return r

    def __make_alias(self):
        return str(uuid.uuid4())[:30].replace('-', '')
