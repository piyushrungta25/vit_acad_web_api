from flask import Flask, jsonify,render_template, request, g, session, flash, redirect, url_for, abort, escape
import psycopg2
import urlparse
import os
from info_api import info_api
from user_management import user_management
from post_management import post_management

# from werkzeug.security import generate_password_hash, check_password_hash

DEBUG = True
SECRET_KEY = os.environ['SECRET_KEY']

app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(info_api)
app.register_blueprint(user_management)
app.register_blueprint(post_management)


def connect_db():
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])

	db = psycopg2.connect(
		database=url.path[1:],
		user=url.username,
		password=url.password,
		host=url.hostname,
		port=url.port
	)


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
	app.run(debug=True)
	# app.run()
