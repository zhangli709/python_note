from socket import socket, SOCK_DGRAM
from time import sleep


def main():
    sender = socket(type=SOCK_DGRAM)  # UDP套接制 速度快，但是容易丢失  1. 创建对象
    with open('zms.jpg', 'rb') as f:
        data = f.read()
        # f.seek()  # 标记，从头移动到尾部
        # f.tell  #
        data_len = len(data)
        total = 0
        while total < data_len:
            sender.sendto(data[total:total+1023], ('10.7.189.77', 8899))
            total += 1024
            sleep(0.0001)


if __name__ == '__main__':
    main()
