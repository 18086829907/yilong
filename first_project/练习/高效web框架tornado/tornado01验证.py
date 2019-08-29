import tornado.web #tornado的基础web框架模块
import tornado.ioloop #tornado的核心IO循环模块，封装了Linux的epoll和BSD的kquque，是tornado高效的基础

#类比django中的视图，是一个业务处理类
class IndexHandler(tornado.web.RequestHandler):
    #处理get请求的
    def get(self, *args, **kwargs):
        #对应http请求的方法
        self.write('jusint is good man') #给客户端响应的数据
    #处理post请求的
    def post(self, *args, **kwargs):
        pass

if __name__ == '__main__':
    #实例化一个应用的对象
    #Application:是tornado web框架的核心应用类，是与服务器对应的接口
    #里面保存了路由映射表
    app = tornado.web.Application([
        (r'/', IndexHandler)
    ])
    #示例化对象的listen方法，功能创建一个http服务器额实例，并绑定了端口
    #注意：此时服务器
    app.listen(8000) #监听端口
    #.IOLoop.current()返回当前线程的IOloop实例，返回一个对象，当前线程读写操作的对象
    #.start()：启动IOLoop实例的I/O循环，同时开始了监听
    tornado.ioloop.IOLoop.current().start()