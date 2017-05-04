from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password
        
class Videos(Base):
    """"""
    __tablename__ = "videos"
 
    id = Column(Integer, primary_key=True)
    video_url = Column(String)
    view_count = Column(Integer)
    image_name = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, video_url, view_count, image_name):
        """"""
        self.video_url = video_url
        self.view_count = view_count
        self.image_name = image_name
		
# create tables
Base.metadata.create_all(engine)


