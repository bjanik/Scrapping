import mysql.connector
import requests

from bs4 import BeautifulSoup

BASE_URL = 'https://pokerdb.thehendonmob.com/'
ALL_TIME_MONEY_LIST_URL = 'https://pokerdb.thehendonmob.com/ranking/all-time-money-list/'

class PokerAllTime:
    
    def __init__(self):
        self.page = None

    @staticmethod
    def load_page(url: str):
        content = requests.get(url)
        if content.status_code == 200:
            page = BeautifulSoup(content.text, 'html.parser')
            return page
    
    @staticmethod
    def getPlayersList(page):
        table = page.find('table', class_='table--ranking-list')
        ranking = table.find_all('tr')
        return ranking

    # We need for each player to get to their ID page and get their highest prize
    def getHighestPrize(self, url):
        page = self.load_page(f'{BASE_URL}/{url}&sort=prize&dir=desc')
        playerResult = page.find('table', class_='table--player-results')
        highestPrice = playerResult.find_all('td', class_='currency')[1].get_text()
        return "".join(highestPrice.split('\n')[1].split('$')[1][1:].split(','))

    @staticmethod
    def getMoney(player):
        money = player.find('td', class_='prize').get_text()
        money = money[2:].split("\n")[0]
        money = "".join(money.split(','))
        return money

    def getPlayersStats(self, playersRanking) -> list:
        players = []
        for player in playersRanking[1:]:
            ranking = player.find('td', class_='place').get_text()[:-2]
            name = player.find('td', class_='name')
            firstName = name.get_text().split()[0]
            lastName = name.get_text().split()[1]
            nationality = player.find('td', class_='flag').get_text()
            money = self.getMoney(player)
            highestPrize = self.getHighestPrize(name.find_all('a')[1]['href'])
            players.append((ranking, firstName, lastName, nationality, money, highestPrize))
        return players

def main():
    poker = PokerAllTime()
    page = poker.load_page(ALL_TIME_MONEY_LIST_URL)
    if page:
        playersRanking = poker.getPlayersList(page)
        players = poker.getPlayersStats(playersRanking)
main()