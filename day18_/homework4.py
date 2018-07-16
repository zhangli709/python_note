from socket import socket
from threading import Thread


def main():
    class RefreshScreenThread(Thread):

        def __init__(self, client):
            super(RefreshScreenThread, self).__init__()
            self._client = client

        def run(self):
            while True:
                data = self._client.recv(1024)
                print(data.decode('utf-8'))  # 一直接受消息并打印出来

    myclient = socket()  # 创建对象
    myclient.connect(('10.7.189.130', 11110))  # 连接服务器
    RefreshScreenThread(myclient).start()  # 刷新接受到的消息
    nickname = input('请输入你的昵称：')
    running = True
    while running:
        content = input('请发言：')
        if content == 'byebye':
            running = False
        else:
            content = nickname + ':' + content
            myclient.send(str(content).encode('utf-8'))  # 发送消息


if __name__ == '__main__':
    main()
