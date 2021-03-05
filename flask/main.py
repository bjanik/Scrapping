import psycopg2
import dotenv
import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)

def createConnection():
    con = psycopg2.connect(
            host=os.environ['PGHOST'],
            user=os.environ['PGUSER'],
            password=os.environ['PGPASSWORD'],
            dbname=os.environ['PGDATABASE'],
            port=os.environ['PGPORT']
    )
    return con

@app.route("/")
def home():
    return "Home"

@app.route("/players")
def players():
    try:
        con = createConnection()
        cursor = con.cursor()
        args = ['ranking', 'money_won', 'country', 'highest_win']
        dico = {
            'ranking': '<=',
            'money_won': '>=',
            'highest_win': '>=',
            'country': ' LIKE '
        }
        d = request.args.to_dict()
        d = {k: v for k,v in d.items() if k in args}
        query = 'SELECT RANKING, FIRST_NAME, LAST_NAME, COUNTRY, MONEY_WON, HIGHEST_WIN FROM ALL_TIME_PLAYERS'
        if d:
            query += " WHERE "
            for c,cond in enumerate(list(d.items())):
                query += f'{cond[0]}{dico[cond[0]]}"{cond[1]}"'
                if c < len(list(d.items())) - 1:
                    query += " AND "
        cursor.execute(query)
        data = cursor.fetchall()
        con.close()
        keys = ('ranking', 'first_name', 'last_name', 'country', 'money_won', 'highest_win')
        players = [{k:v for k,v in zip(keys, d)} for d in data]
        return jsonify({"players" : players})
    except Exception as err:
        return err.__repr__()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ["FLASK_RUN_PORT"], debug=True)
