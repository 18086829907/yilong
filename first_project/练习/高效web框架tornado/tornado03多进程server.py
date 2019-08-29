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
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.bind(800)
    httpserver.start()
    tornado.ioloop.IOLoop.current().start()