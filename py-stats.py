import random
import sys
import os
import numpy as np
import time
import threading
import matplotlib.pyplot as plt
from exchanges import Bitfinex, CoinDesk, Bitstamp


bitcoin_prices = []

for x in range(0, 20):
    price = Bitfinex().get_current_price()
    price = int(float(price))
    start = time.time()
    time.sleep(5)
    bitcoin_prices.append(price)

print bitcoin_prices
plt.plot(bitcoin_prices)
plt.ylabel('BTC Price')
plt.show()


    





