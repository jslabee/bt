#!/usr/bin/env python
import webapp2

from handlers.base import MainHandler
from handlers.TransactionHandler import TransactionHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/transaction', TransactionHandler)

], debug=True)
