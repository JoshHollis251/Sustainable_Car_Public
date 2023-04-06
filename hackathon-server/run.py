# Import flask and datetime module for showing date and time
import os
from flask import Flask, send_from_directory, request

import time
from threading import Thread
import random

from venmo_api import Client
import secret

import messagetext

# Get your access token. You will need to complete the 2FA process
try:
     print("aee")
     access_token = Client.get_access_token(username=secret.username,
                                      password=secret.password,
                                      device_id=secret.device_id)

     venmo = Client(access_token=access_token)
     reciever = venmo.user.get_user_by_username(secret.recieverUser)
except Exception as e:
    print("venmo don't work XD XD XD")
    print(e)

messages = []
speed = 0
rpm = 0
throttle = 0
load = 0

#debug, insert 5 random messages to visualize without waiting for events
def presetMsgs():
    messages.insert(0, {"text": random.choice(messagetext.M_warn_r), "type": "warning"})
    messages.insert(0, {"text": random.choice(messagetext.M_warn_r), "type": "warning"})
    message = random.choice(messagetext.M_charge)
    messages.insert(0, {"text": message, "type": "charge"})
    messages.insert(0, {"text": random.choice(messagetext.M_warn_r), "type": "warning"})
    message = random.choice(messagetext.M_charge)
    messages.insert(0, {"text": message, "type": "charge"})

def checkVals():
    rpmExceeded = False
    rpmTimeExceeded = 0
    rpmWarned = False
    rpmCharged = False
    timeSinceBad = time.time()

    while True:

        global speed, rpm, throttle, load

        now = time.time()
        if rpm > 3000:
            if rpmExceeded == False:
                # start timer, warn user
                rpmExceeded = True
                rpmTimeExceeded = now
            else:
                if ((now - rpmTimeExceeded) >= 1) and not rpmWarned:
                    # uh oh, give them a warning
                    messages.insert(0, {"text": random.choice(messagetext.M_warn_r), "type": "warning"})
                    rpmWarned = True

                if ((now - rpmTimeExceeded) >= 3) and not rpmCharged:
                    # get owned, give them a charge
                    message = random.choice(messagetext.M_charge)
                    messages.insert(0, {"text": message, "type": "charge"})
                    charge(3.00, message)
                    rpmCharged = True
                
        else:
            rpmWarned = False
            rpmExceeded = False
            rpmCharged = False

        if rpmWarned or rpmCharged:
            timeSinceBad = now
        else:
            if (now - timeSinceBad) > 45:
                message = random.choice(messagetext.M_good)
                messages.insert(0, {"text": message, "type": "good"})
                #reimburse(0.01, message)
                timeSinceBad = now

        

        if len(messages) > 7:
            messages.pop()


        
        time.sleep(0.5)


#debug, uncomment to show messages
#presetMsgs()

def charge(amount, message):
     if amount < 5:
          print("YOU ARE ABOUT TO PAY SOME ONE SOME $")
          #time.sleep(5)
          payment_method = venmo.payment.get_payment_methods()[1].id
          venmo.payment.send_money(amount, message, reciever.id, funding_source_id=payment_method) 
     else:
          print("Oh my god you just tried to charge $" + amount)

def reimburse(amount, message):
     if amount < 5:
          payment_method = venmo.payment.get_payment_methods()[1].id
          venmo.payment.request_money(amount, message, reciever.id, funding_source_id=payment_method) 
     else:
          print("Oh my god you just tried to request $" + amount)

# Initializing flask app
app = Flask(__name__, static_url_path='')


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
        
# Route for returning sensor data
@app.route('/data')
def get_data():
    global speed, rpm, throttle, load
    return {
        "speed":speed, 
        "rpm":rpm,
        "throttle":throttle, 
        "load":load
    }

@app.route('/messages')
def get_messages():
    return messages

@app.route('/receive', methods = ["POST"])
def receive_data():
    global speed, rpm, throttle, load
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        speed = int(json["speed"])
        rpm = int(json["rpm"])
        throttle = int(json["throttle"])
        load = int(json["load"])

    return json

      
# Running app
if __name__ == '__main__':
    thread = Thread(target = checkVals)
    thread.daemon = True
    thread.start()
    # IF DEBUG GETS SET TO TRUE IT WILL SPAWN 2 THREADS AND YOU WILL TEAR YOUR HAIR OUT TRYING TO UNDERSTAND THE RACE CONDITIONS
    app.run(debug=False, host="0.0.0.0")