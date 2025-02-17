"""
https://www.tornadoweb.org/en/stable/
"""
import tornado.ioloop
import tornado.web

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(".\\static\\form.html")

    def post(self):
        name = self.get_argument("name")
        self.write(f"Hello, {name}!")

def make_app(*args, **kwargs):
    app = tornado.web.Application([(r"/form", FormHandler)])
    app.listen(8888)
    print("Server started on port 8888")
    tornado.ioloop.IOLoop.current().start()