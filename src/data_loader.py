import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from pathlib import Path

# Declare variables for stock
ticker = "QQQ"
start = "2015-01-02"
end = "2025-12-31"
file_path = Path(f"/home/christian/Projects/Finance/Market-Data-Analyzer/data/{ticker}_{start}_to_{end}.csv")

# If CSV exists, load into pandas
def load_csv():
    df = pd.read_csv(file_path,
        parse_dates=["Date"],
        index_col="Date")
    return df


# If no CSV, create new one
def download_market_data():
    df = yf.Ticker(ticker).history(start=start, end=end)


    try:

        filename = f"{ticker}_{start}_to_{end}.csv"
        if df.empty:
            raise ValueError
        else:
            df.to_csv(file_path)
            print(f"Saved {len(df)} rows to {filename}")
            return df

    except ValueError as e:
        print(f"Data validation error: {e}")
        raise

    except Exception as e:
        print(f"Download failed: {e}")
        raise

def load_market_data():
    # if csv exists, call load_csv
    if file_path.is_file():
        return(load_csv())

    # else csv doesn't exist, call download_data
    else:
        return(download_market_data())

print(load_market_data())
