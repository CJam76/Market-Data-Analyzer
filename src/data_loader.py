import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# Declare variables for stock
ticker = "QQQ"
start = "2015-01-02"
end = "2025-12-31"

# If no CSV, create new one
def download_market_data():


    try:
        df = yf.Ticker(ticker).history(start=start, end=end)
        df.index = df.index.tz_localize(None)
        filename = f"{ticker}_{start}_to_{end}.csv"
        if df.empty:
            raise ValueError
        else:
            df.to_csv(f"data/{filename}")
            print(f"Saved {len(df)} rows to {filename}")
            return df

    except ValueError as e:
        print(f"Data validation error: {e}")

    except Exception as e:
        print(f"Download failed: {e}")


# If CSV exists, load into pandas
def load_csv():
    df = pd.read_csv(f"data/{filename}", parse_data=["Date"], index_col="Date")

print(download_market_data())
