from flask_pymongo import PyMongo
from flask import Flask,jsonify,request, session,redirect, url_for,render_template
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME']='shubhamm0333'
app.config['MONGO_URI']= 'mongodb://chill:chill@ds125578.mlab.com:25578/shubhamm0333'


mongo =PyMongo(app)

@app.route('/',methods=['GET'])
def index():
    if 'username' in session:
         return 'You are logged in as ' + session['username']
    
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login():
    users=mongo.db.users
    login_user=users.find_one({'name':request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),login_user['password'].encode('utf-8'))==login_user['password'].encode('utf-8'):
            session['username']=request.form['username']
            return redirect(url_for('index'))            
    return 'invalid username/password'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method== 'POST':
        users=mongo.db.users

        existing_user = users.find_one({'name':request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'name':request.form['username'],'password':hashpass})
            session['username']=request.form['username']
            return redirect(url_for('index'))

        return 'username already exist'

    return render_template('signup.html')


if __name__=="__main__":
    app.secret_key='mysecret'
    app.run(debug=True)