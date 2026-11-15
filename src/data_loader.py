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
    if filename is not None:
        df.to_csv(f"data/{filename}")
        print(f"Saved {len(df)} rows to {filename}")

    missing_markers = ["n/a", "na", "null", "-", "?", ""]
    df = pd.read_csv(f"data/{filename}", na_values=missing_markers)
    print("Has missing values: ", df.isnull().values.any())

filename = f"{ticker}_{start}_to_{end}.csv"
df = pd.read_csv(f"data/{filename}")
print(df.head(5))
print(df.tail(5))
