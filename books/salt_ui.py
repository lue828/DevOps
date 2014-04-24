#!/usr/bin/env python

import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pymongo
import json
import salt

from tornado.options import define, options
define("port", default=6666, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Salt),
        ]
        #conn = pymongo.Connection("127.0.0.1", 27017)
        #self.db = conn["test"]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class Salt(tornado.web.RequestHandler):
    def get(self):
        results = {}
        self.render('salt_ui.html',title='SaltStack',result=results)

    def post(self):
        print(self.request.remote_ip)
        hostname=self.get_argument('hostname')
        command=self.get_argument('command')
        client = salt.client.LocalClient()
        results = client.cmd(hostname, 'cmd.run', command)
        self.render('salt_ui.html',title='SaltStack', resutl=results)
        #self.render('salt_ui.html',title='SaltStack', **results)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
