from socket import socket, SOCK_DGRAM


def main():
    receiver = socket(type=SOCK_DGRAM)
    receiver.bind(('10.7.189.77', 8899))  # 2.我在这个端口等着你给我数据
    data = bytes()
    while True:
        seg, addr = receiver.recvfrom(1024)  # 3. 收数据，指定缓冲区大小。
        data += seg  # 数据的拼接
        if len(data) >= 27112:
            break
    with open('zms1.jpg', 'wb') as f:
        f.write(data)
    print('图片已接收')
    # receiver.recvfrom()


if __name__ == '__main__':
    main()
