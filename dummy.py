import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","password")
session.add(user)
 
user = User("krishna","krishna")
session.add(user)
 
user = User("ramakanth","ramakanth")
session.add(user)

user = User("shreyas","shreyas")
session.add(user)

user = User("mayank","mayank")
session.add(user)

vid = Videos("http://172.27.196.62:8090/cam1.mjpeg", 0, "frame0.jpg")
session.add(vid)

vid = Videos("http://172.27.196.62:8090/cam2.mjpeg", 0, "frame1.jpg")
session.add(vid)

vid = Videos("http://172.27.196.62:8090/cam3.mjpeg", 0, "frame2.jpg")
session.add(vid)

vid = Videos("http://172.27.253.213:8090/cam1.mjpeg", 0, "frame3.jpg")
session.add(vid)

vid = Videos("http://172.27.144.107:8090/cam1.mjpeg", 0, "frame4.jpg")
session.add(vid)

 
# commit the record the database
session.commit()
