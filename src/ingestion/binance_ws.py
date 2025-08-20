import asyncio
import websockets
import json
import datetime
import os

SYMBOL = "btcusdt"
WS_URL = f"wss://stream.binance.com:9443/ws/{SYMBOL}@depth@100ms"
SAVE_PATH = f"data/raw_ticks/{SYMBOL}.jsonl"

async def collect_orderbook():
    os.makedirs("data/raw_ticks", exist_ok=True)
    async with websockets.connect(WS_URL) as ws:
        with open(SAVE_PATH, 'a') as f:
            while True:
                msg = await ws.recv()
                data = json.loads(msg)
                data['recv_timestamp'] = datetime.datetime.utcnow().isoformat()
                f.write(json.dumps(data) + '\n')

if __name__ == "__main__":
    asyncio.run(collect_orderbook())
