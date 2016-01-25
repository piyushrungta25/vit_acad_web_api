from flask import Flask, jsonify,render_template, request, g, session, flash, redirect, url_for, abort, escape
import MySQLdb
import os
from info_api import info_api
from user_management import user_management
from post_management import post_management

# from werkzeug.security import generate_password_hash, check_password_hash

DEBUG = True
SECRET_KEY =os.urandom(24)

app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(info_api)
app.register_blueprint(user_management)
app.register_blueprint(post_management)

def connect_db():
	db = MySQLdb.connect(host="db4free.net",port=3306,user="piyushrungta25",passwd="d1dd88",db="new_test_db")
	# db = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="password",db="all_posts")
	cur=db.cursor()
	return (db,cur)

@app.before_request
def before_request():
    db,cur=connect_db()
    g.db=db
    g.cur=cur

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    cur = getattr(g, 'cur', None)
    if cur is not None:
        cur.close()
    if db is not None:
		db.close()



if __name__ == '__main__':
	# app.run(debug=True)
	app.run()
