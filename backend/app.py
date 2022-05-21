import sys
import json
import mariadb
import flask
from flask import Flask


app = Flask(__name__)
app.config["DEBUG"] = True

# configuration used to connect to MariaDB
config = {
    'host': '127.0.0.1',
    'port': 3307,
    'user': 'root',
    'password': 'hardpass',
    'database': 'test'
}


@app.route('/api/people', methods=['GET'])
def index():
    # Connection to Mariadb
    con = mariadb.connect(**config)
    # create a connection cursor
    cur = con.cursor()
    # execute a SQL statement
    cur.execute("select * from people")

    # serialize results into JSON
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)


app.run()
