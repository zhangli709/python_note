import urllib
import json
from urllib import request


def get_image(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_image = response.read()
    with open('001.jpg','wb') as fp:
        fp.write(get_image)
        print("download complete")
    return
url = 'http://p2.123.sogoudn.com/imgu/2016/10/20161019124600_428.jpg'
get_image(url)