from flask import Flask, render_template, request, g, session, redirect, url_for, abort, escape, Blueprint
import mailing
import datetime
import os
import random
import string
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
	if 'logged_in' not in session or 'username' not in session:
		session['messages'] =  "No active session"
		return redirect(url_for('user_management.login'))
		
		# template for particular club
	return render_template('home.html')
	

@user_management.route('/signup', methods=['GET', 'POST'])
def signup():
	
	if request.method == 'POST' :
		# validate name and email
		# check if email is unique
		club_name=request.form['CLUBN']
		email=request.form['EMAIL']
		#generate unique key as current timestamp
		unique_key=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(32))
		#send mail with unique key and store in db to verify later
		g.cur.execute("insert into pending_verification(club_name,club_mail,unique_key) values('%s','%s','%s')"%(club_name,email,unique_key))
		g.db.commit()
		subject="Signup request from club %s at VIT clubs portal"%(club_name)
		body='''\
A request has been for registration on VIT clubs portal from your e-mail.  To verify you account follow the following steps.

Post the following message to your facebook page.

    Verification of %s on VIT clubs portal.
    Verification code - %s
    Get your club registered today and reach all vitians through VITacademics app.


'''%(club_name,unique_key)
		mailing.send_mail(subject,body,email)
		
		session['messages']='''Your request has been received. Verification is required for registration!
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
		g.cur.execute("select session_id from login_data where email='%s'"%(session['email']))
		result=g.cur.fetchall()
		result=result[0][0]
		if session['session_id']==result:
			return redirect(url_for('user_management.home'))
			
	
	if request.method == 'POST' :
		g.cur.execute("select * from login_data where email='%s'"%(request.form['USERNAME']))
		result=g.cur.fetchall()
		
		if len(result)<1:
			login_cred_error='Invalid Username'
		elif result[0][2]!=request.form['PASSWORD']:
			login_cred_error='Invalid Password'
		else:
			
			session_id=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(64))
			g.cur.execute("update login_data set session_id='%s' where email='%s'"%(session_id,request.form['USERNAME']))
			g.db.commit()
			session['session_id']=session_id
			session['logged_in'] = True
			session['username']=result[0][0]
			session['email']=result[0][3]
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
