from flask import Flask,render_template,url_for
# from flask_mysqldb import MySQL

app = Flask(__name__)

#connecting to database
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_DB'] = 'pvpsiddh_test'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# mysql = MySQL(app)

@app.route('/event<id>')
def event():
    return render_template('event.html')


@app.route('/')
def home():
    
    
    # cur = mysql.connection.cursor()
    # cur.execute('select * from test')
    # rows = cur.fetchall()
    # cur.close()

    return render_template('home.html',id=1)#rows=rows

@app.route('/members', methods=['GET','POST'])
def members():
    return render_template('members.html')

if __name__=='__main__':
    app.run(debug=True)