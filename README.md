# 🧠 Order Book Replay Simulator

A high-fidelity, tick-by-tick **order book simulator** with **real-time replay**, **web UI**, and support for **trader and algorithm training**.

This project simulates the replay of tick-by-tick market depth data to reconstruct historical order book states. It allows you to:

- Record and store tick data
- Reconstruct and replay historical order books
- Control replay speed and pause/resume for training traders or algorithm testing

---

## Features

- REST API built with FastAPI
- Load historical tick data from JSONL files
- Replay order book state updates with adjustable speed
- Start, pause, and control replay via HTTP endpoints
- Retrieve current order book snapshot at any time

---

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt` (FastAPI, Uvicorn, Requests, etc.)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/orderbook-replay-simulator.git
cd orderbook-replay-simulator

---

## 🔧 Features

- ✅ Record tick-by-tick order book data (Binance)
- ✅ Reconstruct historical Level 2 order book states
- ✅ Replay engine with speed control (1x, 5x, 10x)
- ✅ REST API for playback control (start, pause, speed)
- ✅ React web interface for visualizing the order book
- ✅ Modular design for plugging in strategies or analytics

---

## 📦 Folder Structure


orderbook-replay-simulator/
├── data/ # Raw tick data and snapshots
├── src/ # Python source code
│ ├── ingestion/ # WebSocket data collectors
│ ├── orderbook/ # Order book engine
│ ├── replay/ # CLI replayer
│ ├── api/ # FastAPI server
│ └── ui/ # Optional Streamlit UI
├── ui/ # React frontend
├── tests/ # Unit tests
├── notebooks/ # Data visualization / analysis
├── config.yaml # Symbol and replay settings
├── requirements.txt # Python backend dependencies
├── Dockerfile # Backend container config
└── README.md # This file


---

## 🚀 Quickstart

### ✅ 1. Install Backend

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

uvicorn src.api.main:app --reload

Sample Tick Data Format
{
  "symbol": "AAPL",
  "price": 178.50,
  "volume": 100,
  "side": "buy",
  "timestamp": "2025-08-20T12:34:56"
}


Run the backend server
uvicorn src.api.main:app --reload

Control replay via REST API

Start replay

curl -X POST http://localhost:8000/replay/start


Pause replay

curl -X POST http://localhost:8000/replay/pause


Set replay speed

curl -X POST http://localhost:8000/replay/speed -H "Content-Type: application/json" -d '{"speed": 5.0}'

Open React Web UI

Open http://localhost:3000 in your browser to view the order book visualization.

fastapi==0.95.2
uvicorn[standard]==0.22.0
requests==2.31.0
pydantic==1.10.11
python-dotenv==1.0.0


# API Endpoints

Base URL: `http://localhost:8000`

| Endpoint             | Method | Description                          | Request Body                    | Response                     |
|----------------------|--------|------------------------------------|--------------------------------|------------------------------|
| `/replay/start`      | POST   | Start or resume order book replay  | None                           | `{ "status": "started" }`    |
| `/replay/pause`      | POST   | Pause the replay                    | None                           | `{ "status": "paused" }`     |
| `/replay/speed`      | POST   | Set replay speed                   | `{ "speed": float }`            | `{ "status": "speed set to X" }` |
| `/orderbook/snapshot`| GET    | Get current order book snapshot    | None                           | JSON order book data         |

---

### Example: Start Replay

```bash
curl -X POST http://localhost:8000/replay/start


curl -X POST http://localhost:8000/replay/speed \
  -H "Content-Type: application/json" \
  -d '{"speed": 5.0}'
