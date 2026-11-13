import yfinance as yf
import pandas as pd

ticker = "QQQ"
start = "2015-01-02"
end = "2026-08-30"

df = yf.Ticker(ticker).history(start=start, end=end)

if df.empty:
    print(f"No data returned for {ticker}. Check the symbol or date range.")

else:
    df.index = df.index.tz_localize(None)

    filename = f"{ticker}_{start}_to_{end}.csv"
    df.to_csv(filename)
    print(f"Saved {len(df)} rows to {filename}")
