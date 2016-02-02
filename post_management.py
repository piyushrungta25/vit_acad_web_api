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


@post_management.route('/all_posts')
def all_posts():
	if not valid_session():
		return redirect(url_for('user_management.login'))
	
	g.cur.execute("select * from posts where club_name='%s'"%session['username'])
	posts=g.cur.fetchall()
	
	return render_template('all_posts.html',entries=posts)
	
@post_management.route('/edit_post',methods=['POST'])
def edit_post():
	if not valid_session():
		return redirect(url_for('user_management.login'))
	ts=request.form['timestamp']
	ts=ts.replace(' ','')
	ts=ts.replace('-','')
	ts=ts.replace(':','')
	g.cur.execute('select * from posts where timestamp=%s'%(ts))
	r=g.cur.fetchall()
	r=r[0]
	a=''
	for i in r:
		a=a+str(i)+'<br>'
	
	return a

@post_management.route('/club_info')
def club_info():
	if not valid_session():
		return redirect(url_for('user_management.login'))
	
	g.cur.execute("select * from club_info where club_name='%s'"%(session['username']))
	res=g.cur.fetchall()
	res=res[0]
	return render_template('club_info.html',info=res)

@post_management.route('/edit_info',methods=['POST'])
def edit_info():
	if not valid_session():
		return redirect(url_for('user_management.login'))
	
	g.cur.execute("select * from club_info where club_name='%s'"%(session['username']))
	res=g.cur.fetchall()
	res=res[0]
	a=''
	for i in res:
		a=a+str(i)+'<br>'
	
	return a

# @post_management.route('update_posts',methods=['POST'])
# def update_posts():
	
	# if not valid_login():
		# return redirect(url_for('login'))
	
	# g.cur.execute('UPDATE posts SET timestamp=CURRENT_TIMESTAMP, event_name='event-name',club_name='club_name2',post_body='post-body',event_date='20160202',event_time='03:03:03',event_venue='event-venue',image_link='image-link',event_manager='event-manager',evnt_mngr_phno='event-mngr' where timestamp=20160119202315')
	
	# pass
