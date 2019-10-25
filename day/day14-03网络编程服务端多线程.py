#encoding: utf-8
from socket import socket,SOCK_STREAM,AF_INET
from base64 import b64decode
from  json import  dumps
from threading import Thread

def main():
    class FileTransferThread(Thread):
        def __init__(self,cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()


    # 创建套接字类型，并指定用哪种传输服务
    server  = socket()

    server.bind(('127.0.0.1',5678))
    server.listen(512)
    print('----服务开始监听-----')
    with open('guido.jpg','rb') as f:
        data = b64decode(f.read()).decode('utf-8')
    while True:
        client,addr = server.accept()
        FileTransferThread(client).start()


if __name__ == '__main__':
    main()