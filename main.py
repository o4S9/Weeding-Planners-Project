from flask import Flask, render_template, request,url_for
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt


app = Flask(__name__)




  
 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutpage')
def aboutpage():
    return render_template('about_page.html')

@app.route('/contactus')
def contactus():
    return render_template('contact_page.html')

@app.route('/categary')
def categary():
    return render_template('category_page.html')

@app.route('/signIn')
def signIn():
    return render_template('sign_in_page.html')

@app.route('/signUp')
def signUp():
    return render_template('sign_up_page.html')


@app.route('/forgotPassword')
def forgotPassword():
    return render_template('forgot_password_page.html')

@app.route('/OrderBookPage')
def OrderBookPage():
    return render_template('order_book_page.html')

@app.route('/decor3')
def decor3():
    return render_template('decor3.html')

@app.route('/decor2')
def decor2():
    return render_template('decor2.html')

@app.route('/decor1')
def decor1():
    return render_template('decor1.html')

@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/package1')
def package1():
    return render_template('package_page1.html')

@app.route('/package2')
def package2():
    return render_template('package_page2.html')

@app.route('/package3')
def package3():
    return render_template('package_page3.html')

@app.route('/package4')
def package4():
    return render_template('package_page4.html')

if __name__ == "__main__":
    app.run(debug=True)