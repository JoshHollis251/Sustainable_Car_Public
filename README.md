# Sustainable Car

> An innovative suite of sensors and incentives to encourage sustainable
> and energy efficient driving

Sustainable Car, Abbreviated as Sussycar, was a hackathon project that won 1st place at the UARK Spring 2023 Hackathon, with the theme "sustainability and energy efficiency". It is an app that monitors how you drive, and if you drive in a non-eco-friendly way, it donates money from your Venmo to an organization of the developers' choice.



## Technologies

The project has 3 components: the OBD sender, the backend, and the frontend. 

- **OBD sender**: Written in python, and uses any ELM327-compatible bluetooth OBD2 sensor to connect to your car. It sends POST requests to the backend with the cars' data.

- **Backend**: Receives the messages from the OBD sender and stores them. The computations to determine whether or not the driving is eco-friendly is performed on the backend as well as the connection to Venmo. The backend also serves all of the static content and hosts a basic REST API for the frontend.

- **frontend**: Written in React and uses the recharts graphing library. It queries the backend and provides a live data feed of the driving as well as a past history of the driving messages. 

## Installation

This project requires the following Node.js packages and python packages:

- React
- react-dom
- recharts
- Flask
- venmo-api
- obd

***

### Node.js Dependencies and configuration

Make sure you have Node.js and npm (the Node.js package manager) installed on your system. You can download Node.js from the official website: https://nodejs.org/

navigate to root/hackathon-client and run ```npm install```\
This command will read the package.json file and install the necessary Node.js dependencies listed 

next run ```npm build```\
This command will create a production-ready build of the React frontend in a folder called static within the server's root directory.

***

### Python Dependencies and configuration

Make sure you have Python 3.10 installed on your system. You can download Python from the official website: https://www.python.org/downloads/

install the python modules necessary using either
```
pip install Flask venmo-api obd
```
or
```
python -m pip install Flask venmo-api obd
```
create a secret.py file in root/hackathon-server and include the following information 
```
username = 'your_venmo_username'
password = 'your_venmo_password'
device_id = 'your_device_id'
recieverUser = 'your_reciever_username'
```


## Running The Project

run the application from root/hackathon-server using ```python run.py```

go to the provided localhost on your web browser to view the application



## other notes
please note, the previous repository was made private for privacy concerns. If you wish to see that repository email me at joshuahollis608@gmail.com
