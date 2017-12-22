# Notes
* Drop into docker container: `docker exec -it bc6e60e82de7 /bin/bash`
* Grab environment variables: HOST, PORT, AGENTID
* Repo will have a test-agent (with-example) and API.


```python
import pyba

pyba.init()

# some multi-thread shit?
position = pyba.listen()

if position == foo:
    pyba.move(x=0, y=1)
```
