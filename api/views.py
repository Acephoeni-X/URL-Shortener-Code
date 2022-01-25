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


@api_view(['POST'])
def create(requests):
    s = shortner()
    shortUrl = getattr(s, requests.data['method'])(requests.data['url'])
    data = {
                'url': requests.data['url'],
                'toDomain': requests.data['method'],
                'Ads': True if requests.data['method'] == 'Os' or requests.data['method'] == 'TinyURL' else False,
                'shortUrl': shortUrl
            }
    return Response(data)