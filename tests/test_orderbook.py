import unittest
from book_utils import OrderBook

class TestOrderBook(unittest.TestCase):

    def test_add_and_remove_levels(self):
        ob = OrderBook()
        ob.update_side("bid", 100, 5)
        ob.update_side("ask", 101, 3)

        self.assertEqual(ob.bids[100], 5)
        self.assertEqual(ob.asks[101], 3)

        # Remove bid level
        ob.update_side("bid", 100, 0)
        self.assertNotIn(100, ob.bids)

    def test_update_from_tick(self):
        ob = OrderBook()
        bids = [["100.0", "1.5"], ["99.5", "2.0"]]
        asks = [["101.0", "3.0"], ["101.5", "0.5"]]
        ob.update_from_tick(bids, asks)

        self.assertEqual(ob.bids[100.0], 1.5)
        self.assertEqual(ob.bids[99.5], 2.0)
        self.assertEqual(ob.asks[101.0], 3.0)
        self.assertEqual(ob.asks[101.5], 0.5)

    def test_get_top_n(self):
        ob = OrderBook()
        for i in range(20):
            ob.update_side("bid", 100 - i, i + 1)
            ob.update_side("ask", 101 + i, i + 1)
        top_bids, top_asks = ob.get_top_n(5)
        self.assertEqual(len(top_bids), 5)
        self.assertEqual(len(top_asks), 5)
        self.assertEqual(top_bids[0][0], 100)
        self.assertEqual(top_asks[0][0], 101)

if __name__ == '__main__':
    unittest.main()
