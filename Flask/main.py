from flask import Flask , render_template
import mysql.connector

app = Flask(__name__)

port = 4044

with open("secrets.txt") as f:
    lines = f.readlines()
    host = lines[0].strip()
    user = lines[1].strip()
    password = lines[2].strip()
    database = lines[3].strip()


@app.route('/')
def index():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    mycursor = mydb.cursor()
    mycursor.execute("select tsp, buyPrice from jw order by logid desc limit 5")
    result = mycursor.fetchall
    tsp = []
    buyPrice = []
    for i in mycursor:
        tsp.append(i[0])
        buyPrice.append(float(i[1]))
    return render_template('index.html', pprice=buyPrice[0])


@app.route("/price")
def price():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    mycursor = mydb.cursor()
    mycursor.execute("select tsp, buyPrice from jw order by logid desc limit 5")
    result = mycursor.fetchall
    tsp = []
    buyPrice = []
    for i in mycursor:
        tsp.append(i[0])
        buyPrice.append(float(i[1]))

    return {"time":tsp[0], "price":buyPrice[0]}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)