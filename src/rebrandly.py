import requests
import urllib.parse
from url_shortner import URLShortner, AUTH_TOKEN


class Rebrandly(URLShortner):
    def __init__(self, url):
        super().__init__(url)
        # Must be URL encoded :/
        self.domain = f'https://api.rebrandly.com/v1/links/new?destination={urllib.parse.quote(url)}'
        self.headers = {
            'Accept': 'application/json',
            'apiKey': AUTH_TOKEN
        }

    def shorten_url(self):
        r = {}

        # Need a new way of checking because
        # these few lines are getting repetitive
        if not self.is_valid:
            r['error'] = {
                'message': 'Clipboard content is not a valid url'
            }

            return r

        response = requests.get(self.domain, headers=self.headers)

        # This, too
        if not response.ok:
            return self.process_error(response.status_code)

        r['url'] = response.json()['shortURL']

        return r
