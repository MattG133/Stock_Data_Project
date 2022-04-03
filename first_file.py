import requests
import urrlib3
from bs4 import BeautifulSoup

#TODO: Class/Function to download csvs from STOOQ

ticker = 'art'
start_date = '20100101' # YYYYMMDD
end_date = '20220101' # YYYYMMDD
interval = 'd' # ['d', 'w', 'm', 'q', 'y']

def download_price_data(ticker, start_date, end_date, interval):
    '''
    Downloads csv with stock price data from a given time range
    :param ticker: Ticker of a company on which data to get i.e. CDR (CD Projekt Red
    :param start_date: Date on which to start the range
    :param end_date: Date on which to end the range
    :param interval: Interval for the prices 'd' - day, 'w' - week, 'm' - month, 'q' - quarter, 'y' - year
    :return: nothing, functions saves data to a csv file
    '''
    # customizable url for csv downloa
    download_url = 'https://stooq.pl/q/d/l/?s={}&d1={}&d2={}&i={}'.format(ticker, start_date, end_date, interval)
    # directory to put data in
    directory = '/Users/Maciek/Desktop/Data_Analytics/Stock_Something_Project/data_files/'

    try:
        # request the page
        page = requests.get(download_url, allow_redirects=True)
        # save data to file
        open(directory + ticker + '.csv', 'wb').write(page.content)
        print('Successfully downloaded the data')

    except:
        print('Something went wrong when trying to get {}\n' \
              'Check if the URL is correct or if You are connected to the internet.'.format(download_url))



