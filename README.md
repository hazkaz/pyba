# pyba

Python API for [ByteArena](https://doc.bytearena.com/). Still a work in progress, but it's functional.

Within `test-agent/agent/` is `agent.py` and `pyba.py`.
  * `agent.py` is the agent that will run inside your docker container.
  * `pyba.py` is a Python API for ByteArena.

The provided agent moves around randomly similar to the [example nodejs agent](https://doc.bytearena.com/guides/getting-started/). Here's how it works:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import the pyba ByteArena API
import pyba
import random

# create an instance of the ByteArena class from pyba
comm = pyba.ByteArena()

# start a loop
while True:
    # start getting perception of the world
    if comm.stream("perception"):
        # get a random direction to move in
        direction = random.choice([-1, 1])
        x = direction * random.random()
        y = 3

        # give actions to steer and shoot in this direction
        comm.steer(x, y)
        comm.shoot(x, y)

        # execute those actions
        comm.sendActions()
```
