from exchanges import Bitfinex, CoinDesk

class Bitcoin:
    def get_btc_price(self):
        bitcoin_price = CoinDesk().get_current_price()
c = Bitcoin()
c.get_btc_price()