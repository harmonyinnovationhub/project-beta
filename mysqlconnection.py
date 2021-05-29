from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)
@app.route("/")
def Home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users ")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('index.html', data = fetchdata)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5001", debug = True)