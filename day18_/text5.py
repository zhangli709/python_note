# 做一个联网的应用
# netstat 查看所有端口 telnet连接别人的IP
from socket import socket, AF_INET, SOCK_STREAM
import datetime

def main():
    # 规定：ipv4的协议
    # server = socket(AF_INET, SOCK_STREAM)  可以省略
    # 1.创建一个基于TCP协议的套接字对象。
    # 因为我们做的是应用级的产品或服务，所以可以利用现有的传输服务来实现数据传输。
    server = socket()
    # 2.绑定在IP地址（网络上主机的身份标识），和端口（用来区分不同服务的IP地址的扩展)
    server.bind(('10.7.189.77', 6791))  # 包含ip地址和端口号，对应电脑和服务-应用。
    # 3.开始监听客户端的连接。
    server.listen(512)  # 512 - 为等待队列的大小。
    print('服务器已经启动！正在监听。。。')
    while True:
        # 通过accept方法，接受客户的连接，accept是一个阻塞式的方法：
        # 如果没有客户端连接，那么accept方法会让代码阻塞，直到有客户段连接成功才返回-- 元组，
        # accept 方法返回一个元组，元组中第一个值代表客户端的对象，
        # 元组的第二个值又是一个元组，其中有的客户端的ip地址和端口。
        client, addr = server.accept()
        print(client)
        print(addr, '连接成功')
        t = datetime.datetime.now()
        print(t)
        client.send(str(t).encode('utf-8'))
        #client.close()


if __name__ == '__main__':
    main()