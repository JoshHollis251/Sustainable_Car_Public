import React, { useState, useEffect } from "react";

function Messages(props) {
    const [state, setState] = useState(props.messages)

    
    useEffect(() => {
        setState(props.messages)
    }, [props.messages])

    return (
        <div className="messages-container">
          {state.map((message, index) => (
            <div
              key={`${index}-${message.text}`}
              className={`messagebox ${message.type}`}
              style={{
                animation: `${
                  index === 0 ? "fly-in 0.5s ease-in-out" : "shift-down 0.5s ease-in-out"
                }`
              }}
            >
              <p className="messagetext">{message.text}</p>
            </div>
          ))}
        </div>
      );
}

export default Messages;