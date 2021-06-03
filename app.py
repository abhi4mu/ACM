from flask import Flask,render_template,url_for,request
import flask
from flask_mysqldb import MySQL
import random

app = Flask(__name__)

#connecting to database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'ACM'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


card_colors = ['#abad59','#6f8faf','#9693b2','#deb887','#a14633','#862657','#5b6466','#685a4e','#009440','#fc8eac','#ffa500','#4b0082','#009691']
titles = {1:'Chair',2:'Vice-Chair',3:'Secretary',4:'Treasurer',5:'Web Master',6:'Membership Chair',7:'Student Member'}


@app.route('/alumni',methods=['POST','GET'])
def alumni():

    if request.method == 'GET':
        query = request.args.get('query','')
        return render_template('alumni.html',query=query)
    return render_template('alumni.html')


@app.route('/event/<id>')
def event(id):

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM EVENT_NAMES WHERE EVENT_ID={}".format(id))
    row1 = cur.fetchall()
    cur.execute("SELECT * FROM EVENT_DESC WHERE EVENT_ID={}".format(id))
    row2 = cur.fetchall()
    cur.close()
    return render_template('event.html',row1=row1[0],row2=row2[0])


@app.route('/events')
def events():
    global card_colors

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

    cur = mysql.connection.cursor()
    
    cur.execute('SELECT * FROM CAREER_NEWS')
    careerNews = cur.fetchall()

    cur.execute('SELECT * FROM TECH_NEWS')
    techNews = cur.fetchall()

    cur.close()

    return render_template('home.html',careerNews=careerNews,techNews=techNews)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/members')
def members():

    cur = mysql.connection.cursor()

    cur.execute('SELECT * FROM STUDENT_MEMBERS JOIN STUDENT_YEARS WHERE STUDENT_SNO=SNO AND START_YEAR="2020" AND END_YEAR="2021" ORDER BY TITLE;')
    students = cur.fetchall()

    cur.close()

    for student in students:
        student['TITLE'] = titles[int(student['TITLE'])]#changing numbers to names for titles

    return render_template('members.html',students=students)


if __name__=='__main__':
    app.run(debug=True)
