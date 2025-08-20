from collections import defaultdict
from sortedcontainers import SortedDict

class OrderBook:
    def __init__(self):
        self.bids = SortedDict(lambda x: -float(x))  # Descending
        self.asks = SortedDict()                    # Ascending

    def update(self, bids, asks):
        for price, qty in bids:
            if float(qty) == 0:
                self.bids.pop(price, None)
            else:
                self.bids[price] = qty

        for price, qty in asks:
            if float(qty) == 0:
                self.asks.pop(price, None)
            else:
                self.asks[price] = qty

    def snapshot(self):
        return {
            "bids": list(self.bids.items())[:10],
            "asks": list(self.asks.items())[:10]
        }
