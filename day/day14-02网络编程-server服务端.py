# encoding: utf-8
# requests是一个基于HTTP协议来使用网络的第三库
# 在Python中可以通过创建socket对象并指定type属s性为SOCK_STREAM来使用TCP套接字
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 创建套接字对象并决定使用哪种类型
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET,type = SOCK_STREAM)
    server.bind(('127.0.0.1',6789))
    server.listen(512)
    print('---------监听开始---------')
    while True:
        client,addr = server.accept()
        print(str(addr)+'链接到服务器')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()



if __name__ == '__main__':
    main()
