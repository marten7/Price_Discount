# encoding: utf-8
"""
@version: 1.0
@author: sunjoy
@software: PyCharm
@file: do_wsgi.py
@time: 2020/5/8 7:42 下午
@description: 
"""

from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

httpd = make_server('', 8090, application)
print("Serving HTTP on port 8090...")

httpd.serve_forever()