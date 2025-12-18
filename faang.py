#! /usr/bin/env python

# Computer Innfrastructure Assessment - FAANG Stock Data
# Author: Céaman Collins

import yfinance as yf
import pandas as pd
import datetime as dt
import os
import glob
import platform

def get_data():
    data = yf.download(["META", "AAPL", "AMZN", "NFLX", "GOOG"], period="5d", interval="1h")
    data.to_csv(f"data/{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

get_data()

def plot_data():
    list_of_files = glob.glob('data/*.csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    data = pd.read_csv(latest_file, header=[0, 1], index_col=0, parse_dates=True)
    min_date = data.index.min().strftime('%Y-%m-%d')
    max_date = data.index.max().strftime('%Y-%m-%d')
    title = 'FAANG Stock Prices from ' + min_date +' to ' + max_date
    fig = data.plot(y='Close',
                    title=title,
                    xlabel='Date',
                    ylabel='Closing Price',
                    rot=20,
                    legend=True)
    if platform.system() == "Windows":
        path_to_plots = "plots\\"
        filename = os.path.splitext(latest_file.split('\\')[-1])[0] + ".png"
    else:
        path_to_plots = "plots/"
        filename = os.path.splitext(latest_file.split('/')[-1])[0] + ".png"
    fig.figure.savefig(os.path.join(path_to_plots, filename), dpi=300)

plot_data()
