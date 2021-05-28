from flask import Flask,render_template,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#connecting to database
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'ACM'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/careerNews')
def careerNews():
    return render_template('careerNews.html')

@app.route('/event/<id>')
def event(id):
    return render_template('event.html')


@app.route('/home')
def home():
    
    
    # cur = mysql.connection.cursor()
    # cur.execute('select * from test')
    # rows = cur.fetchall()
    # cur.close()

    return render_template('home.html',id=str(1))#rows=rows

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