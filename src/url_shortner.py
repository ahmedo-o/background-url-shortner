import uuid
import requests
import validators
from env_loader import AUTH_TOKEN


class URLShortner:
    '''
        Default shortner uses TinyURL API (for now)
    '''

    def __init__(self, url):
        self.endpoint = 'https://api.tinyurl.com/create'
        self.auth_keyword = 'api_token'
        self.headers = {}
        self.payload = {
            'url': url,
            'domain': 'tinyurl.com',
            'alias': self.make_alias()
        }
        self._is_valid = False
        self.url = url

    def shorten_url(self):
        r = {}
        if not self.is_valid:
            r['error'] = {
                'message': 'Clipboard content is not a valid url'
            }

            return r

        response = requests.post(
            f'{self.endpoint}?{self.auth_keyword}={AUTH_TOKEN}', data=self.payload)

        if not response.ok:
            return self.process_error(response.status_code)

        r['url'] = response.json()['data']['tiny_url']

        return r

    def make_alias(self):
        # you can change this if you want to change the way you generate an alias
        return str(uuid.uuid4()).split('-')[0]

    def process_error(self, status_code):
        r = {}

        if status_code == 401:
            r['error'] = {
                'message': 'Unauthorized'
            }
        elif status_code == 422:
            r['error'] = {
                'message': 'Invalid URL'
            }
        elif status_code == 429:
            r['error'] = {
                'message': 'Too many requests, try again later'
            }
        elif status_code >= 400 and status_code < 500:
            r['error'] = {
                'message': 'Bad request'
            }
        elif status_code >= 500:
            r['error'] = {
                'message': 'Server error'
            }

        return r

    @property
    def is_valid(self):
        return validators.url(self.url)
