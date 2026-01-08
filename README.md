# Computer Infrastructure Assessment

## Project Summary

The **Computer Infrastructure Assessment** is a coursework project for the ATU module *Computer Infrastructure*. The project demonstrates key skills in data retrieval, visualization, scripting, and automation using Python and GitHub Actions.

You can find the full notebook for this project [here](problems.ipynb).

## Project Description

This project involves solving a series of four tasks designed to enhance proficiency in:
- Fetching financial data using APIs.
- Plotting and analyzing stock data using Python.
- Writing scripts for repeated use and execution from the terminal.
- Automating workflows with GitHub Actions.

## Technologies Used

The project incorporates the following technologies:
- **Python:** For retrieving, processing, and visualizing data.
- **yfinance:** Python library for accessing financial market data.
- **Matplotlib:** Data visualization library for creating stock price charts.
- **GitHub Actions:** For setting up CI automation workflows to run the Python script on a schedule.

## Setup and Installation

To execute the project tasks, ensure you have the required packages installed in a Python environment. You can install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Alternatively, using Conda:

```bash
conda create --name <environment-name> --file requirements.txt
```

The project code can be executed in CodeSpaces, VSCode, or Jupyter Notebook.

## Tasks and Problem Descriptions

### Problem 1: Data from yfinance
Using the yfinance Python package, write a function called `get_data()` that downloads all hourly data for the previous five days for the five FAANG stocks:
- Facebook (META)
- Apple (AAPL)
- Amazon (AMZN)
- Netflix (NFLX)
- Google (GOOG)

The function should save the data into a folder called `data` in the root of your repository using a filename with the format `YYYYMMDD-HHmmss.csv`, where `YYYYMMDD` is the four-digit year (e.g., 20250101) and `HHmmss` is the time.

---

### Problem 2: Plotting Data
Write a function called `plot_data()` that opens the latest data file in the `data` folder and, on one plot, plots the `Close` prices for each of the five stocks. The plot should include axis labels, a legend, and a title.

---

### Problem 3: Script
Create a Python script called `faang.py` in the root of your repository. Copy the above functions into it, so that whenever someone at the terminal types `./faang.py`, the script runs, downloads the data, and creates the plot.

---

### Problem 4: Automation
Create a GitHub Actions workflow to run your script every Saturday morning. The script should be called `faang.yml` in a `.github/workflows/` folder in the root of your repository. In your notebook, explain how and why this workflow works.

---

## Development History and Additional Information

- This project serves as an assessment for the module and encompasses both programming and automation tasks.
- The GitHub Actions workflow is designed to automate data retrieval and processing for the provided tasks weekly.
