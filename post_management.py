from flask import Flask, request, g, Blueprint, session, redirect, url_for, render_template

post_management = Blueprint('post_management', __name__)

@post_management.route('/home', methods=['GET', 'POST'])
def home():
	if 'logged_in' not in session or 'username' not in session or 'session_id' not in session:
		session['messages'] =  "No active session"
		return redirect(url_for('user_management.login'))
		
	g.cur.execute("select session_id from login_data where email='%s'"%(session['email']))
	result=g.cur.fetchall()
	result=result[0][0]
	if session['session_id']==result:
		msg=None
		if 'post_msg' in session:
			msg=session['post_msg']
			session.pop('post_msg', None)
		return render_template('home.html',msg=msg)
	
	else:
		#pop all session entries
		session.pop('logged_in', None)
		session.pop('session_id', None)
		session.pop('username', None)
		session.pop('email', None)
		return redirect(url_for('login'))
	
@post_management.route('/new_post', methods=['POST'])
def new_post():
	
	if request.method == 'POST' :
		#validate input
		event_name=request.form['event-name']
		event_date=request.form['date']
		event_time=request.form['time']
		event_venue=request.form['place']
		event_description=request.form['about']
		event_manager_name=request.form['name']
		event_manager_phoneno=request.form['phno']
		event_image=request.form['image-link']
		
		g.cur.execute("INSERT INTO `all_posts`.`posts` (\
`timestamp` ,\
`club_name` ,\
`event_name` ,\
`post_body` ,\
`event_date` ,\
`event_time` ,\
`event_venue` ,\
`image_link` ,\
`event_manager` ,\
`evnt_mngr_phno`\
)\
VALUES (\
\
CURRENT_TIMESTAMP , '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'\
)"%(session['username'],event_name,event_description,event_date,event_time,event_venue,event_image,event_manager_name,event_manager_phoneno) )
		
		g.db.commit()
		session['post_msg']="New Entry added successfully!"
		return redirect(url_for('post_management.home'))
