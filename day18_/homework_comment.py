from socket import socket
from threading import Thread


def main():
    class Clienthandler(Thread):

        def __init__(self, client):
            super(Clienthandler, self).__init__()
            self._client = client

        def run(self):
            while True:
                try:
                    data = self._client.recv(1024)  # 接受二进制数据

                    for client in clients:
                        client.send(data)
                    #print(data.decode('utf-8'))
                    if data.decode('utf-8') == 'byebye':
                        clients.remove(self._client)
                        self._client.close()
                except Exception as ex_msg:
                    print(ex_msg)
                    clients.remove(self._client)
                    break

    serverce = socket()  # 1. 创建套接制对象
    # AF_INET ip4   SOCK_STREAM = TCP  为默认值。
    # Python 命令行参数-- sys.argv
    serverce.bind(('10.7.189.77', 8891))  # 2. 绑定地址， ip(127.0.0.1\localhost)和ip地址的扩展--端口（1024-65535）
    serverce.listen(512)  # 最大连入数，等待数。
    print('用户连入，开始监听。。。')
    clients = []
    while True:
        cuur_client, addr = serverce.accept()  # 阻塞式的方法，接受用户的请求。
        clients.append(cuur_client)  # 把连入的用户，放到一个列表里。
        Clienthandler(cuur_client).start()


if __name__ == '__main__':
    main()
