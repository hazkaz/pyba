# -*- coding: utf-8 -*-

import json
import os
import socket

class ByteArena():
    def __init__(self):
        self.host = os.environ['HOST']
        self.port = os.environ['PORT']
        self.agentid = os.environ['AGENTID']

        self.actions = []
        self.version = { "version": "clear_beta" }

        # init perception
        self.score = None
        self.energy = None
        self.velocity = None
        self.azimuth = None
        self.vision = None
        self.shootenergy = None
        self.shootcooldown = None
        self.messages = None

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, int(self.port)))
        self.sendHandshake()

    def sendHandshake(self):
        data = {
            "agentid": self.agentid,
            "method":  "Handshake",
            "payload": self.version
        }
        data = (json.dumps(data) + '\n').encode()
        self.s.send(data)

    def sendActions(self):
        data = {
            "agentid": self.agentid,
            "method":  "Actions",
            "payload": { "actions": self.actions }
        }
        data = (json.dumps(data) + '\n').encode()
        self.s.send(data)
        self.actions = []

    def recv(self):
        data = self.s.recv(4096)

        try:
            data = json.loads(data)
        except:
            return

        if data["method"] == "perception":
            payload = data["payload"]
            self.score = payload["score"]
            self.energy = payload["energy"]
            self.velocity = payload["velocity"]
            self.azimuth = payload["azimuth"]
            self.vision = payload["vision"]
            self.shootenergy = payload["shootenergy"]
            self.shootcooldown = payload["shootcooldown"]
            self.messages = payload["messages"]

        return data

    def stream(self, method):
        while True:
            data = self.recv()
            if data and data["method"] == method:
                return True

    def steer(self, x, y):
        action = {
            "method": "steer",
            "arguments": [x, y]
        }
        self.actions.append(action)

    def shoot(self, x, y):
        action = {
            "method": "shoot",
            "arguments": [x, y]
        }
        self.actions.append(action)
