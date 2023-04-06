import obd
import time
import requests

#obd.logger.setLevel(obd.logging.DEBUG)
print("Connecting...")
connection = obd.OBD("//.//COM4", fast=False)
print("Connected.")

while True:
    response = connection.query(obd.commands.RPM)
    rpm = response.value.to("rpm").magnitude
    print("RPM: " + str(rpm))
    response = connection.query(obd.commands.SPEED)
    speed = response.value.to("mph").magnitude
    print("MPH: " + str(speed))
    response = connection.query(obd.commands.THROTTLE_POS)
    throttle = response.value.magnitude
    print("THROTTLE_POS: " + str(throttle))
    response = connection.query(obd.commands.ENGINE_LOAD)
    load = response.value.magnitude
    print("LOAD: " + str(load))
    data = {
        "rpm": rpm,
        "speed": speed,
        "throttle": throttle,
        "load": load
    }
    try:
        requests.post("http://ip:5000/receive", json = data)
    except:
        print("uh oh")
