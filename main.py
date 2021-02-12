import logging
import os
import pathlib
import requests

from bs4 import BeautifulSoup

from logger import logger
from pokerAllTime import PokerAllTime
from pokerdb import handleDB

BASE_URL = 'https://pokerdb.thehendonmob.com/'
ALL_TIME_MONEY_LIST_URL = 'https://pokerdb.thehendonmob.com/ranking/all-time-money-list/'
BRACELETS_WINNERS_URL = 'https://pokerdb.thehendonmob.com/ranking/128/'

LOGFILE = pathlib.Path(f'{os.getcwd()}/logs.log')

logging.basicConfig(filename=LOGFILE,
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')

def main():
    logging.info("Scrapping script starts")
    poker = PokerAllTime()
    page = poker.load_page(ALL_TIME_MONEY_LIST_URL)
    if page:
        playersRanking = poker.getPlayersList(page)
        players = poker.getPlayersStats(playersRanking)
        handleDB(players)
    logging.info("Scrapping script ends")

if __name__ == '__main__':
    main()