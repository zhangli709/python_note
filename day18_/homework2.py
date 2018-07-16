from socket import socket
from threading import Thread


class Send(Thread):

    def __init__(self, client, me):
        super(Send, self).__init__()
        self._client = client
        self._me = me

    def run(self):
        self._client.send(str(self._me).encode('utf-8'))


def main():
    client = socket()  # 1.创建对象
    client.connect(('10.7.189.130', 8080))  # 2.连接服务器
    print('连接成功')
    while True:
        me = input('请输入你要说的话：')  # 发送消息
        #client.send(str(me).encode('utf-8'))
        send = Send(client, me)  # 使用线程
        send.start()
        data = client.recv(1024)
        print(data.decode('utf-8'))


if __name__ == '__main__':
    main()