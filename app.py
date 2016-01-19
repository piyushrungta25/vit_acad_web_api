from flask import Flask, jsonify,render_template, request
import MySQLdb
import time

import datetime

app = Flask(__name__)

def connect_db():
	# db = MySQLdb.connect(host="db4free.net",port=3306,user="piyushrungta25",passwd="d1dd88",db="new_test_db")
	db = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="password",db="all_posts")
	cur=db.cursor()
	return cur

def get_result(cur,timestamp):
	if timestamp==0:
		cur.execute("select count(timestamp) from posts")
		result=cur.fetchall()
		no_of_rows=result[0][0]
		
		print no_of_rows
		if no_of_rows<20:
			cur.execute("select * from posts")
		else:
			cur.execute("select * from posts limit %d,%d"% (no_of_rows-20,20))
		
	else:
		cur.execute("select * from posts where timestamp>%s"%(timestamp))
		
	result=cur.fetchall()
	return result



@app.route('/hello')
def helloception():
	return "helloception"

@app.route('/')
def hello():
	return render_template('index.html')



# @app.route('/get_posts/api/v1.0/get',methods=['GET'])
@app.route('/get_posts/api/v1.0/get',methods=['GET'])
def encode_json():
	cur=connect_db()
	client_timestamp=request.args.get('timestamp',0,type=int)
	results=get_result(cur,client_timestamp)
	result=[]
	
	
	for post in results:
		new_post={
		'timestamp':post[0].isoformat(),
		'club_name':post[1],
		'event_name':post[2],
		'post_body':post[3],
		'event_date':post[4].isoformat(),
		'event_time':(datetime.datetime.min + post[5]).time().isoformat(),
		'event_venue':post[6],
		'image_link':post[7]
		}
		result.append(new_post)
	
	return jsonify({'results':result,'no_of_posts':len(results),'status':'OK'})
	

if __name__ == '__main__':
	app.run(debug=True)
