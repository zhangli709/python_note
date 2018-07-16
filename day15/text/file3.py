# BASE64编码
# json JavaScript Object Notation  http://json.org


def main():

    try:
        with open('abcd/a.jpg', 'rb') as fs1:
            date = fs1.read()
        with open('efg/b.jpg', 'wb') as fs2:
            fs2.write(date)

    except FileNotFoundError:
        print('无法打开')
    except IOError:
        print('读写错误')
    print('程序执行结束')


if __name__ == '__main__':
    main()

