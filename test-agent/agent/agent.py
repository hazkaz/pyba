#!/usr/bin/env python

'''
import pyba
import random

pyba.init()

while True:
    direction = random.choice([-1, 1])
    x = direction * random.random()
    y = float(3)

    pyba.move(x, y)
'''

import random
from pyba import ByteArena

comm = ByteArena()

while True:
    data = comm.recv()

    if data and data["method"] == "perception":
        direction = random.choice([-1, 1])
        x = direction * random.random()
        y = float(3)

        comm.steer(x, y)
