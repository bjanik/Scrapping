import logging
import os
import psycopg2
import sys

from logger import logger

class Database:
    def __init__(self):
        self.dbCon = psycopg2.connect(
            host=os.environ['PGHOST'],
            user=os.environ['PGUSER'],
            password=os.environ['PGPASSWORD'],
            database=os.environ['PGDATABASE'],
            port=os.environ['PGPORT']
        )
        self._cursor = self.dbCon.cursor()

    @logger
    def createTable(self):
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS ALL_TIME_PLAYERS (
                    ID SERIAL PRIMARY KEY,
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

    @logger
    def cleanTable(self):
        self._cursor.execute("TRUNCATE TABLE ALL_TIME_PLAYERS")
        self.dbCon.commit()