from flask import Flask
from flask import render_template
from flask import request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'masterdb.ch0ib4epgaak.us-west-2.rds.amazonaws.com'

mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

for num in range(12000000):  # for monitoring
    cursor.execute("SELECT * from violations limit  5")

data = cursor.fetchall()

conn.commit()


@app.route("/")
def main():

    return render_template('index.html', demodata=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
