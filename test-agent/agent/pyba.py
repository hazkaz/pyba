import json
import os
import socket

# from pyba import ByteArena
# controller = ByteArena()

class ByteArena():
    def __init__(self):
        self.host = os.environ['HOST']
        self.port = os.environ['PORT']
        self.agentid = os.environ['AGENTID']

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, int(self.port)))
        self.handshake()

    def send(self, method, payload):
        data = {
            "agentid": self.agentid,
            "method":  method,
            "payload": payload
        }
        data = (json.dumps(data) + '\n').encode()
        self.s.send(data)

    def recv(self):
        data = self.s.recv(4096)
        try:
            return json.loads(data)
        except: pass

    def handshake(self):
        method = "Handshake"
        payload = { "version": "clear_beta" }
        self.send(method, payload)

    def steer(self, x, y):
        method = "Actions"
        payload = { "actions":[ { "method":"steer", "arguments":[x, y] } ] }
        self.send(method, payload)

'''
#s2 = socket.socket()
#s2.connect((HOST, 1337))

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
        # s2.send(movement)

def init():
    global s
    s = socket.socket()
    s.connect((HOST, int(PORT)))

    handshake = prep("Handshake", { "version": "clear_beta" })
    s.send(handshake)
'''
