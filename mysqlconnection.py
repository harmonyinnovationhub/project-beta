from flask import Flask, render_template, request
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

@app.route('/form', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['users_name']
        lastName = details['users_email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(users_name, users_email) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5001", debug = True)