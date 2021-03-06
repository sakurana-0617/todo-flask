from flask import Flask , render_template ,request,redirect

import random,sqlite3,datetime
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "Flaskå¾©ç¿ð"


@app.route('/greet/<text>')
def greet(text):
    return text + "ããããã«ã¡ã¯"


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    name = "coiai"
    age = 21
    address = "é¦å·ç"
    return render_template("info.html",name=name,age=age,address=address)


@app.route('/weather')
def weather():
    weather = ("æ´ãð","é¨â","æãâ")
    today_weather = random.choice(weather)
    return render_template('weather.html',today_weather=today_weather)
    
    # weather = {'é¦å·':'æ´ã','å¾³å³¶':'é¨','æåª':'æã','é«ç¥':'é¨',}
    # for weather_area in weather
    # today_weather = random.choice(weather[])
    # return render_template('weather.html',today_weather=today_weather)





@app.route('/dbtest')
def dbtest():
    # ãã¼ã¿ãã¼ã¹ã«æ¥ç¶
    connect = sqlite3.connect('flasktest.db')
    cursor = connect.cursor()
    # ãã¼ã¿ãã¼ã¹ã«å½ä»¤
    cursor.execute("SELECT name,age,address FROM user WHERE id = 1")
    user_info = cursor.fetchone()
    connect.close()
    print(user_info)
    return render_template('dbtest.html',html_info = user_info)
    
# methods=["POST"]ã/addã®POSTéä¿¡ã«ãªã
@app.route('/add',methods=["POST"])
def add_post():
    py_task = request.form.get("html_task")
    dt = datetime.datetime.now()
    time = dt.strftime("%y/%m/%d  %Hæ%Må%Sç§")
    connect = sqlite3.connect('flasktest.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO task  VALUES(null, ?, ?)",(py_task, time,))
    # BDãä¿å­
    # data base is locked ã®åå 
    connect.commit()
    connect.close()
    return redirect('/tasklist')

@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/tasklist')
def tasklist():
    connect = sqlite3.connect("flasktest.db")
    cursor = connect.cursor()
    cursor.execute("SELECT id,task,time FROM task")
    task = cursor.fetchall()
    connect.close()
    #taskã®ã¾ã¾ã ã¨ãªã¹ãåã®ä¸­ã«ã¿ãã«åãªã®ã§ä½¿ãã¥ãã
    #ãã®ãããªã¹ãåã®ä¸­ã«è¾æ¸åãæã¤task_listãä½ã
    task_list = []
    for row in task:
        task_list.append({"id":row[0],"task":row[1],"time":row[2]})
    print(task_list)
    return render_template('tasklist.html',html_task=task_list)


@app.route('/edit/<int:id>')
def edit(id):
    connect = sqlite3.connect("flasktest.db")
    cursor = connect.cursor()
    cursor.execute("SELECT task FROM task WHERE id = ?",(id,))
    task = cursor.fetchone()[0]
    connect.close()
    item = {"id":id,"task":task}
    return render_template('edit.html',html_task=item)


@app.route('/edit', methods=['POST'])
def edit_post():
    id = request.form.get('id')
    task = request.form.get('task')
    connect = sqlite3.connect("flasktest.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE task SET task = ? WHERE id = ?", (task, id))
    connect.commit()
    connect.close()
    return redirect('/tasklist')

if __name__ == "__main__":
    app.run(debug=True)