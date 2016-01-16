from flask import Flask, jsonify
import MySQLdb
import time

import datetime

app = Flask(__name__)

def connect_db():
	
	return cur

def get_result(cur,timestamp=None):
	if timestamp==None:
		cur.execute("select * from posts")
		
	else:
		cur.execute("select * from posts where timestamp>%s"%(timestamp))
		
	result=cur.fetchall()
	return result



@app.route('/hello')
def helloception():
	return "helloception"

@app.route('/')
def hello():
	return "This site is under construction. Please come back later."



# @app.route('/get_posts/api/v1.0/get',methods=['GET'])
@app.route('/get_posts/api/v1.0/get')
def encode_json():
	# cur=connect_db()
	# results=get_result(cur)
	db = MySQLdb.connect(host="db4free.net",port=3306,user="piyushrungta25",passwd="d1dd88",db="new_test_db")
	cur=db.cursor()
	cur.execute("select * from posts")
	results=cur.fetchall()
	result=[]
	# return "yo?"
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
	
	return jsonify({'results':result,'status':'OK'})
	



def sample_insertion():
	club_name="club_name"
	event_name="event_name"
	post_body="post_body"
	event_date="event_date"
	event_time="event_time"
	event_venue="event_venue"
	image_link="image_link"

	for i in range(0,10):
		time.sleep(2)
		club_name="club_name"+str(i)
		event_name="event_name"+str(i)
		post_body="postbody"+str(i)
		event_date="2016-0%s-0%s"%(i,i)
		event_time="0%s:0%s:0%s"%(i,i,i)
		event_venue="event_venue"+str(i)
		image_link="image_link"+str(i)
		command="insert into posts (club_name,event_name,post_body,event_date,event_time,event_venue,image_link) values ('%s','%s','%s','%s','%s','%s','%s')"%(club_name,event_name,post_body,event_date,event_time,event_venue,image_link)
		cur.execute(command)
		db.commit()
	
if __name__ == '__main__':
	app.run()
