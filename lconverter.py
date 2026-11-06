#!/usr/bin/env python3

import socket
import sys
import os

def convert_address(hostname: str) -> str:
    if "https" in hostname:
        strip = "https://"
    elif "http":
        strip = "http://"
    hostname = hostname.removeprefix(strip)
    hostname = hostname.removesuffix("/")
    return hostname

if len(sys.argv) == 1:
    print("Usage: <program> link<...>(repeating, infinite args)", sys.stderr)
    os._exit(1)

for i in range(1, (len(sys.argv))):
    if "://" in sys.argv[i] or "/" in sys.argv[i]:
        newaddr = convert_address(sys.argv[i])
        try:
            print(f"{newaddr}: {socket.gethostbyname(convert_address(sys.argv[i]))}")
        except socket.gaierror:
            print(f"{newaddr}: Could not resolve host", file=sys.stderr)
    else: 
        try:
            print(f"{sys.argv[i]}: {socket.gethostbyname(sys.argv[i])}")
        except socket.gaierror:
            print(f"{sys.argv[i]}: Could not resolve host", file=sys.stderr)