import json
import time
from threading import Thread
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from ..orderbook.orderbook import OrderBook  # make sure this import works correctly

app = FastAPI()

# Allow all origins for testing (adjust in production)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Tick(BaseModel):
    symbol: str
    price: float
    volume: int
    side: str
    timestamp: str

# Global variables
book = OrderBook()
ticks = []
tick_index = 0
speed = 1.0
running = False

# Load ticks on startup
@app.on_event("startup")
def load_data():
    global ticks
    with open("data/raw_ticks/btcusdt.jsonl") as f:
        ticks = [json.loads(line) for line in f]

# API endpoints

@app.post("/ticks/")
async def receive_tick(tick: Tick):
    ticks.append(tick.dict())
    return {"message": "Tick received", "tick": tick}

@app.get("/ticks/")
async def get_all_ticks():
    return ticks

@app.get("/simulate/")
@app.post("/simulate/")
async def simulate():
    # Example simulation start
    global running
    if not running:
        running = True
        Thread(target=replay_loop, daemon=True).start()
    return {"message": "Simulation started"}

def replay_loop():
    global tick_index, running
    while running and tick_index < len(ticks):
        tick = ticks[tick_index]
        book.update(tick.get("b", []), tick.get("a", []))  # Assuming tick has 'b' and 'a'
        tick_index += 1
        time.sleep(0.1 / speed)

@app.get("/start")
def start_replay():
    global running
    if not running:
        running = True
        Thread(target=replay_loop, daemon=True).start()
    return {"status": "started"}

@app.get("/pause")
def pause_replay():
    global running
    running = False
    return {"status": "paused"}

@app.get("/speed")
def set_speed(s: float = Query(...)):
    global speed
    speed = s
    return {"speed": speed}

@app.get("/book")
def get_book():
    return book.snapshot()
