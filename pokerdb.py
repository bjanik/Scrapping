import mysql.connector

def createDB():
    dbCon = mysql.connector.connect(
        host='sql_cnt',
        user='root',
        password='totoxxx123',
        auth_plugin='mysql_native_password',
    )
    cursor = dbCon.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS pokerdb;')
    dbCon.commit()
    dbCon.close()

def createTableAndInsert(players):
    dbCon = mysql.connector.connect(
        host='sql_cnt',
        user='root',
        password='totoxxx123',
        auth_plugin='mysql_native_password',
        database='pokerdb'
    )
    cursor = dbCon.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS ALL_TIME_PLAYERS (ID INT PRIMARY KEY AUTO_INCREMENT, RANKING smallint NOT NULL, FIRST_NAME varchar(20), LAST_NAME varchar(20), NATIONALITY varchar(20), MONEY_WON int, HIGHEST_WIN int);')
    cursor.executemany('INSERT INTO ALL_TIME_PLAYERS (RANKING, FIRST_NAME, LAST_NAME, NATIONALITY, MONEY_WON, HIGHEST_WIN) VALUES (%s, %s, %s, %s, %s, %s);', players)
    dbCon.commit()
    dbCon.close()