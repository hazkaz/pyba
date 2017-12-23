#!/usr/bin/env python

import random
from pyba import ByteArena

comm = ByteArena()

while True:
    if comm.recv_until("perception"):
        direction = random.choice([-1, 1])
        x = direction * random.random()
        y = 3

        comm.steer(x, y)
        comm.sendActions()
