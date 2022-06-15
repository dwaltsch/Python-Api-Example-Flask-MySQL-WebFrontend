from flask import Flask , render_template,request
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

@app.route('/dataset-form')
def formset():
    return render_template('selectdataset.html')

@app.route('/dataset-form', methods=['POST'])
def posteddata():
    text = request.form['id']
    string = "select * from jw where Logid = " + str(text)
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    mycursor = mydb.cursor()
    mycursor.execute(string)
    result = mycursor.fetchall
    for i in mycursor:
        logid = i[0]
        tsp = i[1]
        product_id = i[2]
        sellPrice = i[3]
        sellVolume = i[4]
        sellMovingWeek = i[5]
        sellOrders = i[6]
        buyPrice = i[7]
        buyVolume = i[8]
        buyMovingWeek = i[9]
        buyOrders = i[10]
    return {"logid": logid, "timestamp": tsp, "product_id": product_id, "sellPrice": sellPrice,
            "sellVolume": sellVolume, "sellMovingWeek": sellMovingWeek, "sellOrders": sellOrders, "buyPrice": buyPrice,
            "buyVolume": buyVolume, "buyMovingWeek": buyMovingWeek, "buyOrders": buyOrders}

@app.route('/dataset/', methods = ['GET'])
def dataset():
    if request.method == 'GET':
        start = request.args.get('entry_id', default=0, type=int)
        string = "select * from jw where Logid = " + str(start)
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        mycursor = mydb.cursor()
        mycursor.execute(string)
        result = mycursor.fetchall
        for i in mycursor:
            logid = i[0]
            tsp = i[1]
            product_id = i[2]
            sellPrice = i[3]
            sellVolume = i[4]
            sellMovingWeek = i[5]
            sellOrders = i[6]
            buyPrice = i[7]
            buyVolume = i[8]
            buyMovingWeek = i[9]
            buyOrders = i[10]
        return {"logid": logid, "timestamp": tsp,"product_id": product_id,"sellPrice": sellPrice,"sellVolume" : sellVolume, "sellMovingWeek": sellMovingWeek, "sellOrders": sellOrders,"buyPrice": buyPrice,"buyVolume": buyVolume,"buyMovingWeek":buyMovingWeek,"buyOrders":buyOrders}

@app.route("/buyprice")
def buyPrice():
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

@app.route("/sellprice")
def price():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    mycursor = mydb.cursor()
    mycursor.execute("select tsp, sellPrice from jw order by logid desc limit 5")
    result = mycursor.fetchall
    tsp = []
    sellPrice = []
    for i in mycursor:
        tsp.append(i[0])
        sellPrice.append(float(i[1]))

    return {"time":tsp[0], "price":sellPrice[0]}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)