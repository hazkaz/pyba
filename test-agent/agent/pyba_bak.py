import json
import os
import socket

HOST = os.environ['HOST']
PORT = os.environ['PORT']
AGENTID = os.environ['AGENTID']

def incoming(raw):
    try:
        return json.loads(raw)
    except: pass

def prep(method, payload):
    data = { "agentid": AGENTID,
             "method": method,
             "payload": payload }
    return (json.dumps(data) + '\n').encode()

# "method":"Actions","payload":{"actions":[{"method":"steer","arguments":[-0.415577698737708,3]}]}}
def move(x, y):
    blob = incoming(s.recv(4096))

    if blob and blob["method"] == "perception":
        movement = prep("Actions", {"actions":[{"method":"steer", "arguments":[x, y]}]} )
        s.send(movement)

def init():
    global s
    s = socket.socket()
    s.connect((HOST, int(PORT)))

    handshake = prep("Handshake", { "version": "clear_beta" })
    s.send(handshake)
