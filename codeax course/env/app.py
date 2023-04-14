from flask import Flask, flash, redirect, render_template, request, url_for,session
import mysql.connector
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = mysql.connector.connect(host='db4free.net',user='avekisopyeah',password='',database='flasktutorial')
cursor = conn.cursor()

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/coursefree/')
def coursefree():
    return render_template('coursefree.html')


@app.route('/plan/')
def plan():
    return render_template("plan.html")

@app.route('/exploreplan')
def exploreplan():
    return render_template('exploreplan.html')

@app.route('/myvideo/')
def myvideo():
        return render_template('myvideo.html')

@app.route('/contact/')
def contact():
    return render_template('contactus.html')

@app.route('/paidvideo/')
def paidvideo():
    return render_template('paidcourse.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_validator', methods=['POST'])
def login_validator():
    try:
        error = 0
        email = request.form.get('email')
        password = request.form.get('password')

        cursor.execute("""SELECT * FROM `flask_1` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
        users = cursor.fetchall()
        if len(users)>0:
            session['user_id'] = users[0][0]
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html',info = "Invalid Email or password")
    except:
        return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_user',methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    mobile = request.form.get('umobile')
    password = request.form.get('upassword')
    try:

        cursor.execute("""INSERT INTO `flask_1` (`user_id`,`name`,`email`,`mobile`,`password`) VALUES(NULL,'{}','{}','{}','{}')""".format(name,email,mobile,password))
        conn.commit()

        cursor.execute("""SELECT * FROM `flask_1` WHERE `email` LIKE '{}'""".format(email))
        myuser = cursor.fetchall()
        session['user_id'] = myuser[0][0]
        return redirect('/dashboard')
    except:
        return render_template('register.html',error = "Anything went wrong")
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
