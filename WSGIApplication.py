__author__ = 'Liomka'

import Settings

import tornado.web
import tornado.wsgi
import tornado.httpserver


class Application(tornado.wsgi.WSGIApplication):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/demo', JsWSClient),
            (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': "./"}),
            ]
        settings = {
            "site_title": "Liomka.IO",
            "WSServerUrl": Settings.WSSERVER_URI,
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,

            #"ui_modules": {"Entry": EntryModule},
            #"xsrf_cookies": True,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", home="")

class JsWSClient(tornado.web.RequestHandler):
    def get(self):
        self.render("jswsclient.html", js="")