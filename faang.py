# Computer Innfrastructure Assessment - FAANG Stock Data
# Author: Céaman Collins

#! /usr/bin/env computer-infrastructure

import yfinance as yf
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import os
import glob

def get_data():
    data = yf.download(["META", "AAPL", "AMZN", "NFLX", "GOOG"], period="5d", interval="1h")
    data.to_csv(f"data/{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    return data

get_data()

def plot_data():
    list_of_files = glob.glob('data/*.csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    data = pd.read_csv(latest_file, header=[0, 1], index_col=0, parse_dates=True)
    plt.style.use('tableau-colorblind10')
    for stock in data['Close'].columns:
        plt.plot(data['Close'][stock], label=stock)
    plt.legend(loc='best')
    plt.title('FAANG Stock Prices Over the Last 5 Days')
    plt.xticks(rotation=20)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.savefig(f"plots/{os.path.splitext(latest_file)[0][5:]}.png")
    plt.close()

plot_data()
