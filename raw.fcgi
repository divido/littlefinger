#!/usr/bin/env python3
from flipflop import WSGIServer
from raw import app

if __name__ == '__main__':
	WSGIServer(app).run()
