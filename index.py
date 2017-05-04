from flask import Flask, url_for, render_template, Response, Markup,request, redirect, session, flash
import sqlite3
import cv

from functools import wraps

from sqlalchemy.orm import sessionmaker
from tabledef import *

app = Flask(__name__)

curr = 0

# config
app.secret_key = 'my precious'
engine = create_engine('sqlite:///tutorial.db', echo=True)


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            #flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
    
    
# route for handling the login page logic
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
		POST_USERNAME = str(request.form['username'])
		POST_PASSWORD = str(request.form['password'])
	 
		Session = sessionmaker(bind=engine)
		s = Session()

		query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
		result = query.first()
		if result:
			session['logged_in'] = True
			#flash('You were logged in.')
			return redirect(url_for('stream'))
		else:
			error = 'Invalid Credentials. Please try again.'
        
    return render_template('login.html', error=error)
    
    
    

@app.route('/new',methods = ['POST', 'GET'])
def new():
	print(request.form['video_clicked'])
	
	POST_VIDEO_URL = request.form['video_clicked']
	
	conn = sqlite3.connect('tutorial.db')
	c = conn.cursor()
	
	STRING_TO_EXECUTE = 'SELECT * FROM videos WHERE videos.video_url=\'' + POST_VIDEO_URL + '\''
	print(STRING_TO_EXECUTE)
	c.execute(STRING_TO_EXECUTE)
	result = c.fetchone()
	print(result[1])
	
	update = str(result[2] + 1)
	UPDATE_STRING = 'UPDATE videos SET view_count =' + update + ' WHERE videos.video_url=\'' + POST_VIDEO_URL + '\''
	print(UPDATE_STRING)
	c.execute(UPDATE_STRING)
	conn.commit()
	#Session = sessionmaker(bind=engine)
	#s = Session()
	#result = s.query(Videos).filter(Videos.view_count.in_([0])).all()
	#result = Videos.query.filter_by(video_url=POST_VIDEO_URL).first()
	
	
	print('result')
	#print(result)
	return 'count incremented';
	

@app.route('/stream')
@login_required
def stream():
	no_videos = 4	
	current = 0
	mostwatched = []
	allvideosframe = []
	mostwatchedframe = []
	allvideos = []

	
	conn = sqlite3.connect('tutorial.db')
	c = conn.cursor()
	
	COUNT_QUERY = 'SELECT COUNT(*) FROM videos';
	print(COUNT_QUERY)
	c.execute(COUNT_QUERY)
	result = c.fetchone()
	no_videos = result[0]
	print("no_videos")
	print(no_videos)

	
	STRING_TO_EXECUTE = 'SELECT * FROM videos ORDER BY view_count DESC'
	print(STRING_TO_EXECUTE)
	c.execute(STRING_TO_EXECUTE)
	conn.commit()
	for row in c:
		mostwatched.append(row[1])
		mostwatchedframe.append(row[3])
		print(row[1])
		print(row[3])
		
	STRING_TO_EXECUTE = 'SELECT * FROM videos'
	print(STRING_TO_EXECUTE)
	c.execute(STRING_TO_EXECUTE)
	conn.commit()
	for row in c:
		allvideos.append(row[1])
		allvideosframe.append(row[3])
		print(row[1])
		print(row[3])
	
	return render_template('index.html', no_videos=no_videos, mostwatched=mostwatched, current=current, allvideosframe=allvideosframe, allvideos=allvideos, mostwatchedframe=mostwatchedframe)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return render_template('logout.html')


@app.route('/hello')
def hello():
	return render_template('hello.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=4000)
