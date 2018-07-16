def main():

    try:
        with open('abcd/hello.txt', 'a', encoding='utf-8') as fs:
            fs.write('为了梦，何必远方\n')
            fs.write('飞翔')
    except FileNotFoundError:
        print('无法打开')
    except IOError:
        print('读写错误')
    print('程序执行结束')


if __name__ == '__main__':
    main()

