#!/usr/bin/env python
#coding=utf-8
#author:andy
#date:2013-05-08

'''
class for douban song
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

Base = declarative_base()

class Song(Base):
	__tablename__ = 're_songs_tags'
	id = Column(Integer,primary_key = True)
	sid = Column(Integer,nullable=False,unique=True)
	title = Column(String(100),nullable = False)
	artist = Column(String(50),nullable = False)
	tag_id = Column(Integer,nullable = False)

	def __init__(self,sid,title,artist,tag_id):
		self.sid    = sid
		self.title = title
		self.artist = artist
		self.tag_id    =tag_id
	def __repr__(self):
		return "<Song('%s','%s','%s','%d')>" %(self.sid.encode('utf-8'),self.title.encode('utf-8'),self.artist.encode('utf-8'),self.tag_id)

class Tag(Base):
	__tablename__ = 'local_tag_id'
	local_tag_id = Column(Integer,primary_key = True)
	local_tag_name = Column(String(100),nullable = False)
	
	def  __init__(self,tag_id,tag_name):
		self.local_tag_id = tag_id
		self.local_tag_name = tag_name
