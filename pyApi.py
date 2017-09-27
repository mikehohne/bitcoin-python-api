from exchanges.bitfinex import Bitfinex

def get_price():
     Bitfinex().get_current_price()

print get_price()