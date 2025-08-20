import json
from orderbook import OrderBook

book = OrderBook()

with open("data/raw_ticks/btcusdt.jsonl") as f:
    for line in f:
        msg = json.loads(line)
        book.update(msg.get("b", []), msg.get("a", []))  # b = bids, a = asks
        print(book.snapshot())
