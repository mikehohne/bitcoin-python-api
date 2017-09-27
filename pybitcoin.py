from exchanges.bitfinex import Bitfinex

class Bitcoin:
    def get_btc_price(self):
        bitcoin_price = Bitfinex().get_current_price()
        print bitcoin_price
c = Bitcoin()
c.get_btc_price()