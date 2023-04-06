import time
import requests
import random


while True:
    rpm = random.randrange(0, 4000)
    speed = random.randrange(0, 100)
    throttle = random.randrange(0, 100)
    load = random.randrange(0, 100)
    data = {
        "rpm": rpm,
        "speed": speed,
        "throttle": throttle,
        "load": load
    }
    try:
        requests.post("http://localhost:5000/receive", json = data)
    except:
        print("uh oh")
