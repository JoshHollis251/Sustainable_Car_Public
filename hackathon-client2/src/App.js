// Importing modules
import React, { useState, useEffect } from "react";
import Graph from './Graph';
import Messages from './Messages';
import "./App.css";
  
function App() {
    // usestate for setting a javascript

    const [messages, setMessages] = useState([]); 

    // object for storing and using live data
    const [liveData, setLiveData] = useState({
        speed: 0,
        rpm: 0,
        throttle: 0,
        load: 0,
    });

    const [speedHistory, setSpeedHistory] = useState(
        []
    );
    const [rpmHistory, setrpmHistory] = useState(
        []
    );
    const [throttleHistory, setthrottleHistory] = useState(
        []
    );
    const [loadHistory, setloadHistory] = useState(
        []
    );
  
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        const updateData = async () => {
            fetch("/data").then((res) =>
                res.json().then((data) => {
                    // Setting a data from api
                    setLiveData({
                        speed: data.speed,
                        rpm: data.rpm,
                        throttle: data.throttle,
                        load: data.load,
                    });


                    let speedPoint = { uv: data.speed, amt: 2400 };
                    setSpeedHistory((old) => {
                        if (old.length >= 10) {
                            return [...old.slice(1), speedPoint];
                        } else {
                            return [...old, speedPoint];
                        }
                    });

                    let rpmPoint = { uv: data.rpm, amt: 2400 };
                    setrpmHistory((old) => {
                        if (old.length >= 10) {
                            return [...old.slice(1), rpmPoint];
                        } else {
                            return [...old, rpmPoint];
                        }
                    });

                    let throttlePoint = { uv: data.throttle, amt: 2400 };
                    setthrottleHistory((old) => {
                        if (old.length >= 10) {
                            return [...old.slice(1), throttlePoint];
                        } else {
                            return [...old, throttlePoint];
                        }
                    });

                    let loadPoint = { uv: data.load, amt: 2400 };
                    setloadHistory((old) => {
                        if (old.length >= 10) {
                            return [...old.slice(1), loadPoint];
                        } else {
                            return [...old, loadPoint];
                        }
                    });

                    
                })
            );
        }

        const updateMessages = async () => {
            fetch("/messages").then((res) =>
                res.json().then((data) => {
                    setMessages(data)
                })
            );
        };
        
        const interval1 = setInterval(() => {
            updateData();
        }, 500);

        const interval2 = setInterval(() => {
            updateMessages();
        }, 1000);

        return () => {
            clearInterval(interval1);
            clearInterval(interval2);
        }

    }, []);
  
    return (
        <div className="App">
            <div className="logo-container">
                <h1><img className="logo" src="logo2.png" alt="img"/></h1>
            </div>
            <div class="sidebyside">
                <div class="grid2x2 columnleft">
                    <Graph data = {speedHistory} current = {liveData.speed} name = "Speed" threshold = {50}/>
                    <Graph data = {rpmHistory} current = {liveData.rpm} name = "RPM" threshold = {3000}/>
                    <Graph data = {throttleHistory} current = {liveData.throttle} name = "Throttle" threshold = {9999}/>
                    <Graph data = {loadHistory} current = {liveData.load} name = "Engine Load" threshold = {9999}/>
                </div>
                <div class="columnright">
                    <p class="messageheader">Messages</p>
                    <Messages messages={messages} />
                </div>
            </div>
        </div>
    );
}
  
export default App;