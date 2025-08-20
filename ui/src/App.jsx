import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API = "http://localhost:8000";

function App() {
  const [book, setBook] = useState({ bids: [], asks: [] });

  useEffect(() => {
    const interval = setInterval(() => {
      axios.get(`${API}/book`).then(res => setBook(res.data));
    }, 300);
    return () => clearInterval(interval);
  }, []);

  const start = () => axios.get(`${API}/start`);
  const pause = () => axios.get(`${API}/pause`);
  const setSpeed = (s) => axios.get(`${API}/speed?s=${s}`);

  return (
    <div>
      <h1>Order Book Replay</h1>
      <div>
        <button onClick={start}>Start</button>
        <button onClick={pause}>Pause</button>
        <button onClick={() => setSpeed(1)}>1x</button>
        <button onClick={() => setSpeed(5)}>5x</button>
        <button onClick={() => setSpeed(10)}>10x</button>
      </div>
      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
        <div>
          <h2>Bids</h2>
          {book.bids.map(([price, qty]) => (
            <div key={price}>{price} | {qty}</div>
          ))}
        </div>
        <div>
          <h2>Asks</h2>
          {book.asks.map(([price, qty]) => (
            <div key={price}>{price} | {qty}</div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
