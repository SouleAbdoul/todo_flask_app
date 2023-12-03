from flask import Flask,render_template,request,jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)
#app = Flask("test", template_folder='templates')

 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
#mysql = MySQL(app)

 
#Creating a connection cursor
#cursor = mysql.connection.cursor()
 
#Executing SQL Statements
#cursor.execute(''' INSERT INTO todo VALUES('do my job') ''')
 
#Saving the Actions performed on the DB
#mysql.connection.commit()
 
#Closing the cursor
#cursor.close()


#@app.route("/")
#def hello():
#    return render_template("index.html")

#app.run(debug=True)
mysql = MySQL(app)
 
@app.route("/")
def form():
    return render_template("index.html")
 
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        c = mysql.connection.cursor()
        c.execute(''' SELECT * FROM flask_table ''' )
        data = c.fetchall()
        c.close()
        return jsonify(data)
     
    if request.method == 'POST':
        if not request.json or 'task_name' not in request.json:
            return "Error: No taks in JSON request", 400

        task = request.json['task_name']
        #print(task)
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO flask_table (name) VALUES(%s)''',[task])
            #cursor.execute(''' INSERT INTO flask_table VALUES(1,'todo')''')
            mysql.connection.commit()
            cursor.close()

        except Exception as e:
            return f"Database error: {str(e)}", 500

        return f"Done!!"
 
app.run(debug=True)


 
#@app.route('/login', methods = ['POST', 'GET'])
#def login():
#    if request.method == 'GET':
#        return "Login via the login Form"
     
#    if request.method == 'POST':
#        name = request.form['name']
#        age = request.form['age']
#        cursor = mysql.connection.cursor()
#        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
#        mysql.connection.commit()
#        cursor.close()
#        return f"Done!!"
 
#app.run(host='localhost', port=5000)