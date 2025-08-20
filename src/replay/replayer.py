import json
import time
from orderbook import OrderBook

def replay(file_path, speed=1.0, delay=0.1):
    book = OrderBook()
    with open(file_path) as f:
        for line in f:
            tick = json.loads(line)
            book.update(tick.get("b", []), tick.get("a", []))
            snapshot = book.snapshot()
            print("\033[H\033[J", end="")  # Clear screen
            print(f"Time: {tick['recv_timestamp']}")
            print("BIDS:")
            for price, qty in snapshot['bids']:
                print(f"{price} | {qty}")
            print("ASKS:")
            for price, qty in snapshot['asks']:
                print(f"{price} | {qty}")
            time.sleep(delay / speed)

if __name__ == "__main__":
    replay("data/raw_ticks/btcusdt.jsonl", speed=2.0)
