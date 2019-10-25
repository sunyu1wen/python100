#encoding: utf-8
import requests
from time import time
from threading import Thread


class DownloadHandle(Thread):
    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        fileName = self.url[self.url.rfind('/')+1:]
        resp =requests.get(self.url)
        with open('/Users/Hao/'+fileName,'wb') as f:
            f.write(resp.content)


def main():
        resp = requests.get(
        'http://api.tianapi.com/meinv/?key=APIKey&num=10')
