#!/usr/bin/python2.5

"""Application for tracking SLUG user group events."""


import pprint
import logging

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext import db


class IndexPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(template.render(
      'templates/index.html', {}))


application = webapp.WSGIApplication(
  [('/', IndexPage),
   ],
  debug=True)


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
