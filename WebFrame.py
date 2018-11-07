#coding=utf-8
'''
模拟框架程序部分
'''
from socket import *
from views import * 

frame_ip = '127.0.0.1'
frame_port = 8080
frame_address = (frame_ip,frame_port)
#决定我们能处理什么数据
URLS = [('/time',show_time),('/hello',say_hello),('/bye',say_bye)]
#静态网页位置
STATIC_DIR = './static'



#应用类,将功能封装在类中
class Application(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(frame_address)


    def start(self):
        self.sockfd.listen(5)
        print('Listen the port 8080')
        while True:
            connfd,addr = self.sockfd.accept()
            mehtod = connfd.recv(1024).decode()
            path_info = connfd.recv(1024).decode()
            self.handle(connfd,mehtod,path_info)
    
    def handle(self,connfd,mehtod,path_info):
        if mehtod == 'GET':
            if path_info == '/' or path_info[-5:] == '.html':
                response = self.get_html(path_info)
                
            else:
                response = self.get_data(path_info)

        elif mehtod == 'POST':
            pass 
        connfd.send(response.encode())
        connfd.close()
    
    def get_html(self,path_info):
        if path_info == '/':
            get_file = STATIC_DIR + '/index.html'
        else:
            get_file = STATIC_DIR + path_info
        try:
            fd = open(get_file)
        except IOError:
            response = '404'
        else:
            response = fd.read()
        finally:
            return response 

    
    def get_data(self,path_info):
        for url,func in URLS:
            if path_info == url:
                return func()
        return '404'



        



        
        
    










if __name__ == '__main__':
    app = Application()
    app.start() #启动框架应用程序