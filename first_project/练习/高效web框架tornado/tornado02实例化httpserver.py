import tornado.web
import tornado.ioloop
import tornado.httpserver
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('jusint is good man')
    def post(self, *args, **kwargs):
        pass

if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', IndexHandler)
    ])
    # app.listen(8000)
    #手动实例化一个Httpserver对象
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.listen(800)
    tornado.ioloop.IOLoop.current().start()