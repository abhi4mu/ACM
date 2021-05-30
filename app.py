from flask import Flask,render_template,url_for
import flask
from flask_mysqldb import MySQL
import random

app = Flask(__name__)

#connecting to database
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'ACM'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


card_colors = ['#abad59','#6f8faf','#9693b2','#deb887','#a14633','#862657','#5b6466','#685a4e','#009440','#fc8eac','#ffa500','#c0c0c0','#4b0082','#ff033e','#009691']

@app.route('/careerNews')
def careerNews():
    return render_template('careerNews.html')

@app.route('/event/<id>')
def event(id):

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM EVENT_NAMES')
    row1 = cur.fetchall()
    cur.execute('SELECT * FROM EVENT_DESC')
    row2 = cur.fetchall()
    cur.close()
    return render_template('event.html',row1=row1[0],row2=row2[0])


@app.route('/home')
def home():
    global card_colors
    colors_len = len(card_colors)-1

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM EVENT_NAMES ORDER BY START_DATE DESC')
    rows = cur.fetchall()
    cur.close()
    for i in range(len(rows)):
        rows[i]['color'] = card_colors[random.randint(1,colors_len)]

    return render_template('home.html',rows=rows)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/members', methods=['GET','POST'])
def members():
    return render_template('members.html')


@app.route('/techNews')
def techNews():
    return render_template('techNews.html')

if __name__=='__main__':
    app.run(debug=True)
