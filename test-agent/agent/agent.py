#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyba
import random

comm = pyba.ByteArena()

while True:
    if comm.stream("perception"):
        direction = random.choice([-1, 1])
        x = direction * random.random()
        y = 3

        comm.steer(x, y)
        comm.shoot(x, y)
        comm.sendActions()
