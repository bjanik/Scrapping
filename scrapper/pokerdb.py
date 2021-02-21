import logging
import mysql.connector
import os
import sys

from logger import logger

class Database:
    def __init__(self):
        self.dbCon = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            auth_plugin='mysql_native_password',
            database=os.environ['MYSQL_DATABASE']
        )
        self._cursor = self.dbCon.cursor()

    @logger
    def createTable(self):
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS ALL_TIME_PLAYERS (
                    ID INT PRIMARY KEY AUTO_INCREMENT,
                    RANKING smallint NOT NULL,
                    FIRST_NAME varchar(20),
                    LAST_NAME varchar(20),
                    COUNTRY varchar(20),
                    MONEY_WON int,
                    HIGHEST_WIN int);""")
        self.dbCon.commit()

    @logger
    def insertInTable(self, data):
        self._cursor.execute("""INSERT INTO ALL_TIME_PLAYERS (RANKING, FIRST_NAME, LAST_NAME, COUNTRY, MONEY_WON, HIGHEST_WIN) VALUES (%s, %s, %s, %s, %s, %s)""", data)
        self.dbCon.commit()
