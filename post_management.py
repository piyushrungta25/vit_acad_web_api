from flask import Flask, request, g, Blueprint

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
		return render_template('home.html')
	
	else:
		#pop all session entries
		return redirect(url_for('login'))
	
@post_management.route('/temp', methods=['GET', 'POST'])
def new_post():
	return 'new'
