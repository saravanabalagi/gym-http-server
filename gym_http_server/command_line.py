#!/usr/bin/env python3
from gym_http_server import start_server
from gym_http_server import __version__
import argparse

def main():
    parser = argparse.ArgumentParser(description='Start a Gym HTTP API server')
    parser.add_argument('-l', '--listen', help='interface to listen to', default='127.0.0.1')
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to bind to')
    parser.add_argument('-v', '--version', action='version', 
                                version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    start_server(listen=args.listen, port=args.port)

if __name__ == '__main__':
    main()