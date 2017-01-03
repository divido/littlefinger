#!/usr/bin/env python3
import sys
sys.stderr = open('/tmp/littlefinger-raw-stderr.txt', 'w')

from flipflop import WSGIServer
from raw import app

if __name__ == '__main__':
	WSGIServer(app).run()
