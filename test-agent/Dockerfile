FROM python:3

# /usr/src/app is the root of our code in the container
WORKDIR /usr/src/app

# After API is in PyPi
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# Bundle our source code in the container
COPY . /usr/src/app/

# Tell Docker how to run our code
CMD [ "python", "./agent/agent.py" ]
