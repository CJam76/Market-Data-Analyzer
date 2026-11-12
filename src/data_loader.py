import yfinance as yf
import pandas as pd

def qqq_data():
    qqq = yf.Ticker("QQQ")
    return(qqq.info)

print(qqq_data)
