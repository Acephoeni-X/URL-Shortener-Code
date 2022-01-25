from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pyshorteners

class shortner():
    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def chilpit(self, url):
        return self.shortener.chilpit.short(url)

    def Clck(self, url):
        return self.shortener.clckru.short(url)

    def Da(self, url):
        return self.shortener.dagd.short(url)

    def Is(self, url):
        return self.shortener.isgd.short(url)

    def Os(self, url):
        return self.shortener.osdb.short(url)

    def TinyURL(self, url):
        return self.shortener.tinyurl.short(url)

@api_view(['GET'])
def index(requests, protocol, url, method):
    s = shortner()
    url = url.replace('%20', '/').replace(' ', '/')
    short = {
                'chilpit': s.chilpit(url = f'{protocol}://{url}'),
                'Clck': s.Clck(url = f'{protocol}://{url}'),
                'Da': s.Da(url = f'{protocol}://{url}'),
                'Is': s.Is(url = f'{protocol}://{url}'),
                'Os': s.Os(url = f'{protocol}://{url}'),
                'TinyURL': s.TinyURL(url = f'{protocol}://{url}'),
            }
    data = {
        'data' : {
                    'name': url,
                    'toDomain': method,
                    'Ads': True if method == 'Os' or method == 'TinyURL' else False,
                    'shortUrl': short[f'{method}']
                 }
    }

    return Response(data)