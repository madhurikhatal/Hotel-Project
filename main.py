#from os import name
from flask import Flask, app,render_template,request
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import query
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123@localhost/event'
#db = SQLAlchemy(app)
'''
class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(75),nullable=False)
    last_name = db.Column(db.String(75),nullable=False)
    address = db.Column(db.String(75),nullable=False)
    aadhar_no = db.Column(db.BIGINT)
    email = db.Column(db.String(75),nullable=False)
    phone_number = db.Column(db.Integer,nullable=False)
    bed_type = db.Column(db.String(30),nullable=False)
    Accomodation = db.Column(db.String(30),nullable=False)
    checkin_time = db.Column(db.DateTime())
    checkout_time =db.column(db.DateTime())
    payment = db.Column(db.String(30),nullable=False)
    isactive = db.Column(db.Boolean, default=False, nullable=False)

class Cont(db.Model):
     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
     name =  db.Column(db.String(75),nullable=False)
     mail = db.Column(db.String(75),nullable=False)   
     query =  db.Column(db.String(75),nullable=False)
     isactive = db.Column(db.Boolean, default=False, nullable=False)
db.create_all()
'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/book')
def book():
    return render_template('book.html')
    
@app.route('/booking')
def booking():
    return render_template('booking.html')
    
@app.route('/cake')
def cake():
    return render_template('cake.html')

@app.route('/chef')
def chef():
    return render_template('chef.html')

@app.route('/cont',methods=['GET','POST'])
def cont():
    return render_template('cont.html')
    
@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/guest')
def guest():
    return render_template('guest.html')

@app.route('/indiaan2')
def indian2():
    return render_template('indian2.html')

@app.route('/italian')
def italian():
    return render_template('italian.html')

"""@app.route('/login/')
def login():
    return render_template('login.html')"""

@app.route('/meeting')
def meeting():
    return render_template('meeting.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/party')
def party():
    return render_template('party.html')

@app.route('/pool')
def pool():
    return render_template('pool.html')
    
@app.route('/reegister')
def register():
    return render_template('register.html')

@app.route('/southindian')
def southindian():
   
    return render_template('southindian.html')

app.run(debug= True,port=8000)
    
    
    
    
    
    
    
    
    
    
    
    
        