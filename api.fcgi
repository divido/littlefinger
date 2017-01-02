#!/usr/bin/env python3

import sys
sys.stdout = open('/tmp/littlefinger-api-stdout.txt', 'w')
sys.stderr = open('/tmp/littlefinger-api-stderr.txt', 'w')

from flipflop import WSGIServer
from api import app

if __name__ == '__main__':
	WSGIServer(app).run()
