import pandas as pd
import matplotlib.pyplot as plt


def test():

    '''
    Creates a Pandas data table containing the Adj Close price between a date range specified in the function

    You can change the start date and end date to alter the output table. The stocks used are SPY, AAPL, IBM and GLD
    however you can use any you wish, I recommend downloading the csv files from Yahoo Finance. This script will
    strip any NaN values in the first join, which means weekends and public holidays are stripped from the output.
    '''

    start_date = '2011-01-01'
    end_date = '2016-01-01'
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)

    '''
    Import financial data, using the Date col as index, retrieving Date and Adj Close,
    and converting NaN into a string
    '''

    dfSPY = pd.read_csv('data/SPY.csv', index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    '''
    Join csv data to the data frame, dropping 'na' values (NaN strings indicated when CSVs are imported)
    '''

    df = df.join(dfSPY, how='inner')
    df = df.rename(columns={'Adj Close': 'SPY'})

    '''
    Read in the remaining stock details
    '''

    symbols = ['AAPL', 'IBM', 'GLD']

    for symbol in symbols:
        df_temp = pd.read_csv('data/{}.csv'.format(symbol), index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

    '''
    Plot this data to a line graph, set up labels and titles
    '''

    df.plot()
    plt.xlabel("Date")
    plt.ylabel("Price in USD")
    plt.title("A comparison of Adjusted Close prices for four stocks")
    plt.show()

if __name__ == '__main__':
    test()