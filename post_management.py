from flask import Flask, request, g, Blueprint, session, redirect, url_for, render_template

post_management = Blueprint('post_management', __name__)

def valid_session():
	if 'logged_in' not in session or 'username' not in session or 'session_id' not in session or 'email' not in session:
		# session['messages'] =  "No active session"
		return False

	g.cur.execute("select session_id from login_data where email='%s'"%(session['email']))
	result=g.cur.fetchall()
	result=result[0][0]
	if session['session_id']==result:
		return True

	else:
		#pop all session entries
		session.pop('logged_in', None)
		session.pop('session_id', None)
		session.pop('username', None)
		session.pop('email', None)
		return False
		# return redirect(url_for('login'))

@post_management.route('/home', methods=['GET', 'POST'])
def home():
	if not valid_session():
		# session['messages'] =  "No active session"
		return redirect(url_for('user_management.login'))

	msg=None
	if 'post_msg' in session:
		msg=session['post_msg']
		session.pop('post_msg', None)
	return render_template('home.html',msg=msg)

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

		g.cur.execute("INSERT INTO posts (\
timestamp,\
club_name ,\
event_name ,\
post_body ,\
event_date ,\
event_time ,\
event_venue ,\
image_link ,\
event_manager ,\
evnt_mngr_phno\
)\
VALUES (\
\
now()::timestamp(0) without time zone,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'\
)"%(session['username'],event_name,event_description,event_date,event_time,event_venue,event_image,event_manager_name,event_manager_phoneno) )

		g.db.commit()
		session['post_msg']="New Entry added successfully!"
		return redirect(url_for('post_management.home'))


@post_management.route('/all_posts')
def all_posts():
	if not valid_session():
		return redirect(url_for('user_management.login'))
	msg=None
	if 'post_msg' in session:
		msg=session['post_msg']
		session.pop('post_msg', None)
	g.cur.execute("select * from posts where club_name='%s'"%session['username'])
	posts=g.cur.fetchall()

	return render_template('all_posts.html',entries=posts,msg=msg)

@post_management.route('/edit_post',methods=['POST'])
def edit_post():
	if not valid_session():
		return redirect(url_for('user_management.login'))
	ts=request.form['timestamp']

	g.cur.execute("select * from posts where timestamp='%s'"%(ts))
	res=g.cur.fetchall()
	post=res[0]


	return render_template("edit_post.html",post=post)

@post_management.route('/club_info')
def club_info():
	if not valid_session():
		return redirect(url_for('user_management.login'))
	msg=None
	if 'update_msg' in session:
		msg=session['update_msg']
		session.pop('updatet_msg', None)
	g.cur.execute("select club_info.*, login_data.email from club_info \
join login_data \
on login_data.club_name = club_info.club_name where club_info.club_name='%s'"%(session['username']))
	res=g.cur.fetchall()
	res=res[0]
	return render_template('club_info.html',info=res,msg=msg)

@post_management.route('/edit_info',methods=['POST'])
def edit_info():
	if not valid_session():
		return redirect(url_for('user_management.login'))

# 	g.cur.execute("UPDATE club_info set club_logo='%s',\
# club_desc='%s',\
# contact_info='%s',\
# where club_name='%s'" % (request.form['logo'],request.form['about'],request.form['contact_info'],session['username']) )
#
# 	g.db.commit()
# 	g.cur.execute("UPADTE login_data set email='%s' where club_name='%s'"%(request.form['email'],session['username']))
# 	g.db.commit()

	session['update_msg']="Club info updated successfully!"
	return redirect(url_for('post_management.club_info'))

@post_management.route('/update_posts',methods=['POST'])
def update_post():

	if not valid_session():
		return redirect(url_for('login'))

	event_name=request.form['event-name']
	event_date=request.form['date']
	event_time=request.form['time']
	event_venue=request.form['place']
	event_description=request.form['about']
	event_manager_name=request.form['name']
	event_manager_phoneno=request.form['phno']
	event_image=request.form['image-link']
	current_timestamp=request.form['timestamp']
	query="UPDATE posts set timestamp=now()::timestamp(0) without time zone,\
event_name='%s',\
post_body='%s',\
event_date='%s',\
event_time='%s',\
event_venue='%s',\
image_link='%s',\
event_manager='%s',\
evnt_mngr_phno='%s'\
where timestamp='%s'" % (event_name,event_description,event_date,event_time,event_venue,event_image,event_manager_name,event_manager_phoneno,current_timestamp)

	g.cur.execute(query)
	g.db.commit()
	session['post_msg']="Event updated successfully!"
	return redirect(url_for('post_management.all_posts'))
