from flask import Flask, request, g, Blueprint

post_management = Blueprint('post_management', __name__)

@post_management.route('/home', methods=['GET', 'POST'])
def home():
	if 'logged_in' not in session or 'username' not in session:
		session['messages'] =  "No active session"
		return redirect(url_for('user_management.login'))
		
		# template for particular club
	return render_template('home.html')
	
@post_management.route('/temp', methods=['GET', 'POST'])
def new_post():
	return 'new'
