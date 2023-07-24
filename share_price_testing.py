# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:11:46 2023

@author: joema
"""

# testing chnages

import yfinance as yf
import matplotlib.pyplot as plt

hwg_close = yf.download('HWG.L IUKP.L', start='2020-01-01', end = None)['Close']

plt.plot(hwg_close)
plt.legend(hwg_close)
plt.savefig('HWG v IUKP Share Price from 2020-01 to 2023-07.png')