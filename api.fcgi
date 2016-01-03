#!/usr/bin/env python3
from flipflop import WSGIServer
from api import app

if __name__ == '__main__':
    WSGIServer(app).run()
