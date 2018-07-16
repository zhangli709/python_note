import socket
from datetime import datetime
import re


def main():

    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host,port))

    s.listen(5)
    while True:
        c, addr = s.accept()
        print('连接地址',addr)
        c.send('hello')
        c.close()

if __name__ == '__main__':
    main()
