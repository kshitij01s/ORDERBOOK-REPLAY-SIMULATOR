import React from 'react';
import axios from 'axios';

const API = "http://localhost:8000";

function Controls() {
  const start = () => axios.get(`${API}/start`);
  const pause = () => axios.get(`${API}/pause`);
  const setSpeed = (speed) => axios.get(`${API}/speed?s=${speed}`);

  return (
    <div className="controls">
      <button onClick={start}>Start</button>
      <button onClick={pause}>Pause</button>
      <button onClick={() => setSpeed(1)}>1x</button>
      <button onClick={() => setSpeed(5)}>5x</button>
      <button onClick={() => setSpeed(10)}>10x</button>
    </div>
  );
}

export default Controls;
