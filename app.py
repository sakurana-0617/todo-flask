from flask import Flask , render_template ,request,redirect

import random,sqlite3
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "Flask復習📔"


@app.route('/greet/<text>')
def greet(text):
    return text + "さんこんにちは"


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    name = "coiai"
    age = 21
    address = "香川県"
    return render_template("info.html",name=name,age=age,address=address)


@app.route('/weather')
def weather():
    weather = ("晴れ🌞","雨☔","曇り⛅")
    today_weather = random.choice(weather)
    return render_template('weather.html',today_weather=today_weather)
    
    # weather = {'香川':'晴れ','徳島':'雨','愛媛':'曇り','高知':'雨',}
    # for weather_area in weather
    # today_weather = random.choice(weather[])
    # return render_template('weather.html',today_weather=today_weather)





@app.route('/dbtest')
def dbtest():
    # データベースに接続
    connect = sqlite3.connect('flasktest.db')
    cursor = connect.cursor()
    # データベースに命令
    cursor.execute("SELECT name,age,address FROM user WHERE id = 1")
    user_info = cursor.fetchone()
    cursor.close()
    print(user_info)
    return render_template('dbtest.html',html_info = user_info)
    
# methods=["POST"]が/addのPOST通信になる
@app.route('/add',methods=["POST"])
def add_post():
    py_task = request.form.get("html_task")
    connect = sqlite3.connect('flasktest.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO task  VALUES(null, ?)",(py_task,))
    # BDを保存
    # data base is locked の原因
    connect.commit()
    cursor.close()
    return redirect('/')

@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)