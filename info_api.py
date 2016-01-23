from flask import Flask, jsonify, request, g, Blueprint
import urllib
import datetime

info_api = Blueprint('info_api', __name__)	


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

@info_api.route('/vitwebapp/api/v1.0/get_posts',methods=['GET'])
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


@info_api.route('/vitwebapp/api/v1.0/get_clubinfo',methods=['GET'])
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
