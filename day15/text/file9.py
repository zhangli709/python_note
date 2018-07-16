import json
import requests


def main():
    resp = requests.get('http://api.tianapi.com/nba/?key=81085f5747a59581327b29d1bccfb925&num=10')
    mydict = json.loads(resp.text)
    print(mydict)
    for tempdict in mydict['newslist']:
        pic_url = tempdict['picUrl']
        resp = requests.get(pic_url)
        filename = pic_url[pic_url.rfind('/') + 1:]
        try:
            with open(filename, 'wb') as fs:
                fs.write(resp.content)
        except IOError as e:
            print(e)


if __name__ == '__main__':
    main()

