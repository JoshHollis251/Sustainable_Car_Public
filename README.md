# Sustainable Car

> An innovative suite of sensors and incentives to encourage sustainable
> and energy efficient driving

Sustainable Car, Abv. Sussycar, was a hackathon project that won 1st place at the UARK Spring 2023 Hackathon, with the theme "sustainability and energy efficiency". It is an app that monitors how you drive, and if you drive in a non-eco-friendly way, it donates money from your Venmo to an organization of the developers' choice.



## Technologies

The project has 3 components: the OBD sender, the backend, and the frontend. 

The OBD sender is written in python, and uses any ELM327-compatible bluetooth OBD2 sensor to connect to your car. It sends POST requests to the backend with the cars' data.

The backend receives the messages from the OBD sender and stores them. The computations to determine whether or not the driving is eco-friendly is performed on the backend as well as the connection to Venmo. The backend also serves all of the static content and hosts a basic REST API for the frontend.

The frontend is written in React and uses the recharts graphing library. It queries the backend and provides a live data feed of the driving as well as a past history of the driving messages. 

## Installation

1. Make sure you have Python 3.10 installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. install the python modules necessary using either
```
pip install Flask venmo-api obd
```
or
```
python -m pip install Flask venmo-api obd
```
3. create a secret.py file in root/hackathon-server and include the following information 
```
username = 'your_venmo_username'
password = 'your_venmo_password'
device_id = 'your_device_id'
recieverUser = 'your_reciever_username'
```

4. run the application from root/hackathon-server using ```python run.py```

5. go to the provided localhost on your web browser to view the application

## other notes
please note, the previous repository was made private for privacy concerns. If you wish to see that repository email me at joshuahollis608@gmail.com
