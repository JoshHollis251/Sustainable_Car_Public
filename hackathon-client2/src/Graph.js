import { LineChart, Line, CartesianGrid, XAxis, YAxis, ResponsiveContainer, ReferenceLine } from 'recharts'
import React, { useState, useEffect } from "react";

function Graph(props) {
    const [state, setState] = useState(props.data)

    
    useEffect(() => {
        setState(props.data)
    }, [props.data])

    return (       
    <div>
        {props.current > props.threshold ?
            <p className="displaydata">{props.name}:    <span className="exceeded">{props.current}</span></p>
        :
            <p className="displaydata">{props.name}:    <span className="data_entry">{props.current}</span></p>
        }
        <ResponsiveContainer aspect={2}>
            <LineChart data={state} margin={{top: 20, right: 20, left: 20, bottom: 20}}>
                <Line type="linear" animationDuration={0} dataKey="uv" stroke="#8884d8" strokeWidth="3pt" />
                <ReferenceLine y={props.threshold} stroke="red" strokeWidth="3pt"/>
                <CartesianGrid stroke="#ccc" />
                <XAxis dataKey="name" />
                <YAxis />
            </LineChart>
        </ResponsiveContainer>
    </div> 
    );
}

export default Graph;