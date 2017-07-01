# coding:utf8

from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import urllib
import re


class Test(object):
    def __init__(self):
        pass

    def download(url):
        try:
            headers = {'User-agent': 'Mozilla/5.0'}
            request = urllib.request.Request(url, headers=headers)
            req = urlopen(request).read()
            html = BS(req, 'html.parser')
        except Exception as e:
            print(e)
            html = None
        except urllib.request.URLError as e:
            print(e.reason)
            html = None
            if e.errno == re.compile(r'^5*'):
                return Test.download('http://www.baidu.com')
        return html