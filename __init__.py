
from flask import Flask
from flask.ext.mysql import MySQL


app = Flask(__name__)

'''mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cs411fa2016'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)'''

@app.route("/hello")
def hello():
    return "Hello VirtualVoyager!"

if __name__ == "__main__":
    app.run()

