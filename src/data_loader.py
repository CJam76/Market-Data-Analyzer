import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from pathlib import Path

# Declare variables for stock
ticker = "QQQ"
start = "2015-01-02"
end = "2025-12-31"
df = yf.Ticker(ticker).history(start=start, end=end)
df.index = df.index.tz_localize(None)

# If CSV exists, load into pandas
def load_csv():
    df = pd.read_csv("/home/christian/Projects/Finance/Market-Data-Analyzer/data/QQQ_2015-01-02_to_2025-12-31.csv")

# If no CSV, create new one
def download_market_data():


    try:

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

def load_market_data():
    file_path = Path("/home/christian/Projects/Finance/Market-Data-Analyzer/data/QQQ_2015-01-02_to_2025-12-31.csv")

    # if csv exists, call load_csv
    if file_path.is_file():
        load_csv()

    # else csv doesn't exist, call download_data
    else:
        download_market_data()

print(load_market_data())
