import React, { useState, useEffect } from "react";
import GameBoard from "./Gameboard";
import { aiMove } from "./AIPlayer";

function App() {
  const [state, setState] = useState({});
  const [ws, setWs] = useState(null);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/player1");
    socket.onmessage = (event) => {
      try {
        setState(JSON.parse(event.data.replace(/'/g, '"')));
      } catch {
        console.log(event.data);
      }
    };
    setWs(socket);
  }, []);

  const sendMove = () => {
    ws.send("move_forward");
  };

  return (
    <div>
      <h1>AI Multiplayer Game</h1>
      <button onClick={sendMove}>Move Forward</button>
      <GameBoard state={state} />
    </div>
  );
}

export default App;
