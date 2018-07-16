from socket import socket


def main():
    client = socket()
    client.connect(('10.7.189.77', 6790))
    data = client.recv(1024)
    print(type(data))
    print(data.decode('utf-8'))
    sentence = client.send('hello'.encode('utf-8'))



if __name__ == '__main__':
    main()