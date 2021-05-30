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


card_colors = ['#abad59','#6f8faf','#9693b2','#deb887','#a14633','#862657','#5b6466','#685a4e','#009440','#fc8eac','#ffa500','#4b0082','#009691']

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

@app.route('/events')
def events():
    global card_colors
    colors_len = len(card_colors)-1

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM EVENT_NAMES ORDER BY START_DATE DESC')
    rows = cur.fetchall()
    cur.close()

    # from now the code is adding randomly generated colors to cards in rows dictionary
    availableColors = set() #with this set we make sure no color is repeated until all colors are selected

    for i in range(len(rows)):
        if not availableColors:#if set is empty i.e; no colors available
            availableColors = set(card_colors) #filling set with colors
        color = random.sample(availableColors,1)#getting 1 color from set as list
        availableColors.remove(color[0])#removing obtained color from set
        rows[i]['color'] = color[0]
    #adding colors finished

    return render_template('events.html',rows=rows)


@app.route('/home')
def home():
    return render_template('home.html')

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
