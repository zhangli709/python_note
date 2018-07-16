import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=81085f5747a59581327b29d1bccfb925&num=10')
    mydict = json.loads(resp.text)  # 将网页上的文本获取
    for tempdict in mydict['newslist']:
        pic_url = tempdict['picUrl']
        resp = requests.get(pic_url)  # 存放请求到的内容
        filename = pic_url[pic_url.rfind('/') + 1:]  # 拿文件名
        try:
            with open(filename, 'wb') as fs:
                fs.write(resp.content)  # contet,属性，拿二进制数据。
        except IOError as e:
            print(e)


if __name__ == '__main__':
    main()