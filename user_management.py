from flask import Flask, render_template, request, g, session, redirect, url_for, abort, escape, Blueprint
import mailing

user_management = Blueprint('user_management', __name__)	


@user_management.route('/logout')
def logout():
	if 'logged_in' not in session:
		session['messages'] =  "No active session"
		return redirect(url_for('user_management.login'))
	
	session.pop('logged_in', None)
	session.pop('username', None)
	session['messages'] = "Logged out successfully!"
	return redirect(url_for('user_management.login'))
	


@user_management.route('/home', methods=['GET', 'POST'])
def home():
	if 'logged_in' not in session:
		session['messages'] =  "No active session"
		return redirect(url_for('user_management.login'))
		
		# template for particular club
	return render_template('home.html')
	

@user_management.route('/signup', methods=['GET', 'POST'])
def signup():
	
	if request.method == 'POST' :
		# validate name and email
		club_name=request.form['CLUBN']
		email=request.form['EMAIL']
		
		#send mail with unique key and store in db to verify later
		
		session['messages']='''Your request has been sent\nVerification is required for registration!\
Please follow the steps given in the mail to complete your registration'''
		
	return redirect(url_for('user_management.login'))

@user_management.route('/login', methods=['GET', 'POST'])
@user_management.route('/', methods=['GET', 'POST'])
def login():
	login_cred_error = None
	forget_pass_error = None	
	msg=None
	signup_error=None
	
	if 'messages' in session:
		msg=session['messages']
		session.pop('messages', None)
	
	if 'forget_pass_error' in session:
		forget_pass_error=session['forget_pass_error']
		session.pop('forget_pass_error', None)
	
	if 'signup_error' in session:
		signup_error=session['forget_pass_error']
		session.pop('signup_error', None)
	
	
	
		
	if 'logged_in' in session:
		return redirect(url_for('user_management.home'))
	
	if request.method == 'POST' :
		g.cur.execute("select * from login_data where username='%s'"%(request.form['USERNAME']))
		result=g.cur.fetchall()
		
		if len(result)<1:
			login_cred_error='Invalid Username'
		elif result[0][2]!=request.form['PASSWORD']:
			login_cred_error='Invalid Password'
		else:
			session['logged_in'] = True
			session['username']=result[0][0]
			return redirect(url_for('user_management.home'))
	
	return render_template('index.html', login_cred_error=login_cred_error,msg=msg,forget_pass_error=forget_pass_error,signup_error=signup_error)


@user_management.route('/reset_password',methods=['POST'])
def reset_password():
	error=None
	if request.method == 'POST' :
		
		g.cur.execute("select * from login_data where email='%s' and club_name='%s'"%(request.form['MAILID'],request.form['CLUB_NAME']))
		result=g.cur.fetchall()
		
		if len(result)==0:
			session['forget_pass_error'] = "Invalid E-mail and Club Name combination!"
			return redirect(url_for('user_management.login'))
			
		elif len(result)==1:
			# send the email with password
			#
			result=result[0]
			subject="Password reset on VIT Club Portal for %s"%(request.form['CLUB_NAME'])
			body='''\
A password reset was requested for this e-mail on VIT Club Portal.
The current password is
%s
Resetting password is highly recommended.

Thank You
VIT Clubs Portal Team
'''%(str(result[2]))
			receiver=request.form['MAILID']
			mailing.send_mail(subject,body,receiver)
			#
			# handle exceptions
			session['messages'] = "Password reset successful. Password sent to %s."%(request.form['MAILID'])
			return redirect(url_for('user_management.login'))
		
		else:
			#log the multiple email error
			pass
	
	# add not allowed to access this page since no get request
	return redirect(url_for('user_management.login'))
