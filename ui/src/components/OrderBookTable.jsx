import React from 'react';

function OrderBookTable({ bids, asks }) {
  return (
    <div className="orderbook">
      <div>
        <h2>Bids</h2>
        <ul>
          {bids.map(([price, qty]) => (
            <li key={price}>{price} | {qty}</li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Asks</h2>
        <ul>
          {asks.map(([price, qty]) => (
            <li key={price}>{price} | {qty}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default OrderBookTable;
