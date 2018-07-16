from socket import socket
from threading import Thread


class Accept(Thread):

    def __init__(self, client):
        super(Accept, self).__init__()
        self._client = client

    def run(self):
        data = self._client.recv(1024)
        return print(data.decode('utf-8'))


class Send(Thread):

    def __init__(self, client, sentence):
        super(Send, self).__init__()
        self._sentence = sentence
        self._client = client

    def run(self):
        self._client.send(str(self._sentence).encode('utf-8'))


def main():
    server = socket()  # 创建对象
    server.bind(('10.7.189.77', 6672))  # 绑定IP和端口
    server.listen(512)  # 同时连入数，最大等待数
    print('程序已经启动，正在监听。。。。')
    while True:
        client, addr = server.accept()  # 接受连入的对象，前面为服务器的地址，后面为客户端的IP
        print(addr, '已经连接')
        while True:
            accept = Accept(client)  # 使用线程接受消息
            accept.start()
            # print(data.decode('utf-8'))
            #data = client.recv(1024)
            #print(data.decode('utf-8'))

            t = input('请输入你要发送的话：')  # 发送消息
            send = Send(client, t)
            send.start()


if __name__ == '__main__':
    main()

