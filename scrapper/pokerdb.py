import logging
import mysql.connector
import os
import sys

from logger import logger



class HandleDB:
    def __init__(self, db_name):
        self.dbCon = mysql.connector.connect(
            host='sql_cnt',
            user='root',
            password='totoxxx123',
            auth_plugin='mysql_native_password',
            database=db_name
        )
        self._cursor = self.dbCon.cursor()

    @logger
    def createTable(self):
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS ALL_TIME_PLAYERS (
                    ID INT PRIMARY KEY AUTO_INCREMENT,
                    RANKING smallint NOT NULL,
                    FIRST_NAME varchar(20),
                    LAST_NAME varchar(20),
                    NATIONALITY varchar(20),
                    MONEY_WON int,
                    HIGHEST_WIN int);''')
        self.dbCon.commit()

    @logger
    def insertTable(self, players):
        self._cursor.executemany('''INSERT INTO ALL_TIME_PLAYERS
                       (RANKING, FIRST_NAME, LAST_NAME, NATIONALITY, MONEY_WON, HIGHEST_WIN)
                       VALUES (%s, %s, %s, %s, %s, %s);''', players)
        self.dbCon.commit()


@logger
def handleDB(players=[]):
    try:
        db = HandleDB('pokerdb')
        db.createTable()
        db.insertTable(players)
        db.dbCon.close()
    except mysql.connector.Error as err:
        logging.error(f'{err}')
        db.dbCon.close()
        sys.exit(1)
