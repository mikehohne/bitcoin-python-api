import datetime
from exchanges import Bitfinex, Bitstamp

class Bitcoin:
    def get_btc_price(self):
        bf_bitcoin_price = Bitfinex().get_current_price()
        bs_bitcoin_price = Bitstamp().get_current_price()
        print bf_bitcoin_price, bs_bitcoin_price
c = Bitcoin()
c.get_btc_price()