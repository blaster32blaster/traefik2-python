import time

# import redis
from flask import Flask

app = Flask(__name__)

def get_hit_count():
    while True:
        return 3

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)