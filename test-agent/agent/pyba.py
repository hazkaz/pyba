import json
import os
import socket

HOST = os.environ['HOST']
PORT = os.environ['PORT']
AGENTID = os.environ['AGENTID']

def prep(data):
    return (json.dumps(data) + '\n').encode()

def listen(s):
    while True:
        s.recv(1024)

def init():
    s = socket.socket()
    s.connect((HOST, int(PORT)))

    handshake = { "agentid": AGENTID,
                  "method": "Handshake",
                  "payload": { "version": "clear_beta" } }

    handshake = prep(handshake)
    s.send(handshake)

    listen(s)
