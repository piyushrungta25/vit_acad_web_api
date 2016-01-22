from flask import Flask, jsonify,render_template, request, g, session, flash, redirect, url_for, abort, escape
import MySQLdb
import time
import urllib
import datetime
# import os

DEBUG = True
# SECRET_KEY =os.urandom(24)
SECRET_KEY ='key'

app = Flask(__name__)
app.config.from_object(__name__)

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
    if db is not None and cur is not None:
        cur.close()
        db.close()
    



def get_result(timestamp):
	if timestamp==0:
		g.cur.execute("select count(timestamp) from posts")
		result=g.cur.fetchall()
		no_of_rows=result[0][0]
		
		print no_of_rows
		if no_of_rows<20:
			g.cur.execute("select * from posts")
		else:
			g.cur.execute("select * from posts limit %d,%d"% (no_of_rows-20,20))
		
	else:
		g.cur.execute("select * from posts where timestamp>%s"%(timestamp))
		
	result=g.cur.fetchall()
	return result



@app.route('/hello')
def helloception():
	return "helloception"

# @app.route('/')
# def hello():
	# return render_template('index.html')


@app.route('/vitwebapp/api/v1.0/get_posts',methods=['GET'])
def get_posts():
	client_timestamp=request.args.get('timestamp',0,type=int)
	results=get_result(client_timestamp)
	result=[]
	
	
	for post in results:
		g.cur.execute("select club_logo from club_info where club_name='%s'"%post[1])
		logo=g.cur.fetchall()
		logo=logo[0][0]
		
		new_post={
		'timestamp':post[0].isoformat(),
		'club_name':post[1],
		'event_name':post[2],
		'post_body':post[3],
		'event_date':post[4].isoformat(),
		'event_time':(datetime.datetime.min + post[5]).time().isoformat(),
		'event_venue':post[6],
		'image_link':post[7],
		'club_logo':logo
		}
		result.append(new_post)
	
	return jsonify({'results':result,'no_of_posts':len(results),'status':'OK'})
	

@app.route('/vitwebapp/api/v1.0/get_clubinfo',methods=['GET'])
def get_club_info():
	club_name=request.args.get('club_name','')
	urllib.unquote(club_name)
	club_info=[]
	
	if club_name=='':
		#implement error
		return jsonify({'result':club_info,'status':'EMPTY_NAME'})
	
	
	
	g.cur.execute("select * from club_info where club_name='%s'"%(club_name))
	results=g.cur.fetchall()
	
	if len(results)<1:
		return jsonify({'result':club_info,'status':'WRONG_NAME'})
		
	result=results[0]
	
	club_info=[{
	'club_name':result[0],
	'club_logo':result[1],
	'club_description':result[2],
	'contact_detais':result[3]
	}]
	return jsonify({'result':club_info,'status':'OK'})


@app.route('/home', methods=['GET', 'POST'])
def home():
	if 'logged_in' not in session:
		return redirect(url_for('login'))
	return 'logged_in'


# @app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	
	if 'logged_in' in session:
		return redirect(url_for('home'))
	
	if request.method == 'POST' :
		g.cur.execute("select * from login_data where username='%s'"%(request.form['USERNAME']))
		result=g.cur.fetchall()
		
		if len(result)<1:
			error='Invalid Username'
		elif result[0][2]!=request.form['PASSWORD']:
			error='Invalid Password'
		else:
			session['logged_in'] = True
			session['username']=result[0][0]
			flash('You were logged in')
			return redirect(url_for('home'))
	
	return render_template('index.html', error=error)


if __name__ == '__main__':
	app.run(debug=True)
