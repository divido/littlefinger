#!/usr/bin/env python3

import sys
sys.stderr = open('/tmp/littlefinger-api-stderr.txt', 'w')

import logging
logging.basicConfig(filename='/tmp/littlefinger-api.log', level=logging.DEBUG, filemode='w')

from flipflop import WSGIServer
from api import app

if __name__ == '__main__':
	logging.info('Starting up the API service')
	WSGIServer(app).run()
