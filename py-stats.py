import random
import sys
import os
import numpy as np
import time
import matplotlib.pyplot as plt
from pybitcoin import Bitcoin

bitcoin_prices = []

for x in range(0, 2):
    price = Bitcoin().get_btc_price()
    bitcoin_prices.append(price)

print (bitcoin_prices)
    
# plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
# plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
# plt.xlim(0.5, 4.5)
# plt.show()



