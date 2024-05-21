from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import bcrypt
import MySQLdb.cursors
from flask_mysqldb import MySQL
import random
import datetime
import pytz



app = Flask(__name__)
app.secret_key = 'your_secret_key'



# MySQL configurations
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "user-system"



# Configure Flask-Mail
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'sendm6319@gmail.com'
app.config["MAIL_PASSWORD"] = 'rltb wdxx ymqo ilsb'



mysql = MySQL(app)
mail = Mail(app)
s = URLSafeTimedSerializer(app.secret_key)



@app.route('/')
def index():
    return render_template('signup.html')



@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html')
    return redirect(url_for('login'))




@app.route('/login', methods=['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully!'
            return render_template('home.html', mesage=mesage)
        else:
            flash ('Please enter correct email / password!')
    return render_template('login.html', mesage=mesage)




@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        confirm = request.form.get('confirm')
        if confirm == 'yes':
            # Clear session variables
            session.pop('loggedin', None)
            session.pop('userid', None)
            session.pop('email', None)
            
           
            flash('You have been logged out.')
            
            
            resp = make_response(redirect(url_for('login')))
            resp.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            resp.headers['Pragma'] = 'no-cache'
            resp.headers['Expires'] = '0'
            return resp
        else:
            return redirect(url_for('home'))  
    return render_template('logout_confirm.html')




OTP_EXPIRATION_TIME = 60  # OTP expiration time in seconds (1 minute)

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        userName = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        password2 = request.form.get('password2')
        
        if not all([userName, password, email, password2]):
            message = 'Please fill out all fields!'
        elif len(password) < 8:
            message = 'Password must be at least 8 characters long!' 
        elif password != password2:
            message = 'Passwords do not match!'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
            account = cursor.fetchone()
            
            if account:
                message = 'Account already exists!'
            else:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cursor.execute('INSERT INTO user(name, email, password) VALUES (%s, %s, %s)', 
                               (userName, email, hashed_password.decode('utf-8')))
                mysql.connection.commit()
                cursor.close()
                
                otp = random.randint(100000, 999999)
                session['email_verification_otp'] = otp
                session['email_verification_email'] = email
                session['otp_generation_time'] = datetime.datetime.now(pytz.utc).isoformat()

                msg = Message('Email Verification', sender=app.config["MAIL_USERNAME"], recipients=[email])
                msg.body = f"Hi {userName},\nYour email OTP is: {otp}"
                mail.send(msg)
                
                return render_template('user_email_verify.html', email=email)
    return render_template('signup.html', message=message)



@app.route('/user_email_otp_verify', methods=['POST'])
def email_verify():
    user_otp = request.form.get('otp')
    email = session.get('email_verification_email')
    otp = session.get('email_verification_otp')
    otp_generation_time_str = session.get('otp_generation_time')
    
    if email and otp and otp_generation_time_str:
        otp_generation_time = datetime.datetime.fromisoformat(otp_generation_time_str).replace(tzinfo=pytz.utc)
        current_time = datetime.datetime.now(pytz.utc)

        if (current_time - otp_generation_time).total_seconds() > OTP_EXPIRATION_TIME:
            flash("OTP has expired. Please request a new OTP.")
            session.pop('email_verification_otp', None)
            session.pop('otp_generation_time', None)
            return render_template('user_email_verify.html', email=email)
        
        if int(user_otp) == otp:
            session.pop('email_verification_otp', None)
            session.pop('email_verification_email', None)
            session.pop('otp_generation_time', None)
            flash("Your email is verified. You can login now!")
            return redirect(url_for('login'))
        else:
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute('DELETE FROM user WHERE email = %s', (email,))
                mysql.connection.commit()
            
            session.pop('email_verification_otp', None)
            session.pop('email_verification_email', None)
            session.pop('otp_generation_time', None)
            flash("Your email verification has failed. Register with a valid Email!")
            return redirect(url_for('register'))
    else:
        flash("Invalid session data. Please try again.")
        return redirect(url_for('register'))




    



@app.route('/user_forgot', methods=['GET', 'POST'])
def user_forgot():
    
    if 'loggedin' in session:
        return redirect(url_for('home'))
    mesage = ''
    if request.method == 'POST':
        email = request.form['email']
        cursor = mysql.connection.cursor()
        result = cursor.execute("SELECT * FROM user WHERE email = %s", [email])
        if result > 0:
            token = s.dumps(email, salt='password-reset')
            msg = Message('Password Reset', sender=app.config['MAIL_USERNAME'], recipients=[email])
            link = url_for('reset', token=token, _external=True)
            msg.body = f'Your password reset link is {link}'
            mail.send(msg)
              
            flash('A password reset link has been sent to your email address.')
            return redirect(url_for('user_forgot'))
        else:
            flash ("Email does not exist")
    return render_template('forgot_password.html', mesage=mesage)




@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset(token):
    if 'loggedin' in session:
        return redirect(url_for('home'))
    
    try:
        email = s.loads(token, salt='password-reset', max_age=3600)
    except SignatureExpired:
        flash("The password reset link has expired.")
        return redirect(url_for('user_forgot'))
    
    if request.method == 'POST':
        password = request.form['password']
        confirm_password = request.form['confirm_password']
    
        
        if password != confirm_password:
            flash("Passwords don't match.")            
        elif len(password) < 8:
            flash('Password must be at least 8 characters long!')
            return redirect(url_for('reset', token=token))
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        user = cursor.fetchone()
        
        if user:
            cursor.execute("UPDATE user SET password = %s WHERE email = %s", (hashed_password.decode('utf-8'), email))
            mysql.connection.commit()
            flash("Your password has been successfully updated.")
            return redirect(url_for('login'))
        else:
            flash("Invalid or expired token.")
            return redirect(url_for('user_forgot'))
    return render_template('reset.html')







if __name__ == "__main__":
    app.run(debug=True)
