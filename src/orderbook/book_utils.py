from sortedcontainers import SortedDict

class OrderBook:
    def __init__(self):
        # SortedDict with price as key and quantity as value
        # Bids sorted descending, Asks ascending
        self.bids = SortedDict(lambda x: -x)  # descending order
        self.asks = SortedDict()               # ascending order

    def update_side(self, side: str, price: float, qty: float):
        book_side = self.bids if side == "bid" else self.asks
        if qty == 0:
            if price in book_side:
                del book_side[price]
        else:
            book_side[price] = qty

    def update_from_tick(self, bids: list, asks: list):
        # bids and asks are list of [price_str, qty_str]
        for price_str, qty_str in bids:
            price = float(price_str)
            qty = float(qty_str)
            self.update_side("bid", price, qty)
        for price_str, qty_str in asks:
            price = float(price_str)
            qty = float(qty_str)
            self.update_side("ask", price, qty)

    def get_top_n(self, n=10):
        top_bids = list(self.bids.items())[:n]
        top_asks = list(self.asks.items())[:n]
        return top_bids, top_asks

    def snapshot(self):
        # Returns full book snapshot as dict
        return {
            "bids": list(self.bids.items()),
            "asks": list(self.asks.items()),
        }
