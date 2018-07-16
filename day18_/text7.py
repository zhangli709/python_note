import json
import requests
from threading import Thread


class PictureLoad(Thread):

    def __init__(self, url):
        super(PictureLoad, self).__init__()
        self._url = url

    def run(self):

        resp = requests.get(self._url)
        filename = self._url[self._url.rfind('/') + 1:]
        try:
            with open(filename, 'wb') as fs:
                fs.write(resp.content)
        except IOError as e:
            print(e)


def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=81085f5747a59581327b29d1bccfb925&num=10')
    my_dict = json.loads(resp.text)
    threads = []
    for temp in my_dict['newslist']:
        pic_url = temp['picUrl']
        pictureload = PictureLoad(pic_url)
        pictureload.start()
        #resp = PictureLoad(pic_url).start()
        threads.append(pictureload)
    for thread in threads:
        thread.join()
    print('图片下载完成')



if __name__ == '__main__':
    main()