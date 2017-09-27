import random
import sys
import os
import numpy as np
import time
import threading
import matplotlib.pyplot as plt
from exchanges import Bitfinex, Bitstamp


bf_bitcoin_prices = []
bs_bitcoin_price = []

for x in range(0, 30):
    bf_price = Bitfinex().get_current_price()
    bs_price = Bitstamp().get_current_price()
    bf_price = int(float(bf_price))
    bs_price = int(float(bs_price))
    start = time.time()
    time.sleep(2)
    bf_bitcoin_prices.append(bf_price)
    bs_bitcoin_price.append(bs_price)

plt.plot(bf_bitcoin_prices, label='Bitfinex')
plt.plot(bs_bitcoin_price, label="Bitstamp")
plt.xlabel('Time')
plt.ylabel('BTC Price $')
plt.title('Bitcoin Exchange Prices\nPast 15 minutes')
plt.legend()
plt.show()


    





