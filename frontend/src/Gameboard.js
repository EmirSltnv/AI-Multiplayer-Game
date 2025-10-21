import React from "react";

function GameBoard({ state }) {
  return (
    <div>
      <h2>Game Board</h2>
      {Object.keys(state).map((pid) => (
        <div key={pid}>
          <strong>{pid}</strong> - Position: {state[pid].position} | Score: {state[pid].score}
        </div>
      ))}
    </div>
  );
}

export default GameBoard;
