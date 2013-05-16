#!/usr/bin/env python
#coding:utf-8
#author:andy
#date:2013-05-08

from song import Song,Tag
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from log import TTLog



db_config = {
	'host':'192.168.6.8',
	'user':'ttpod',
	'passwd':'ttpod123',
	'db':'douban',
	'charset':'utf8'
	}
class DBHelper:
	def  __init__(self):
		self.engine=create_engine('mysql://%s:%s@%s/%s?charset=%s'%(db_config['user'],db_config['passwd'],db_config['host'],db_config['db'],db_config['charset']),echo=False)
		Session = sessionmaker(bind = self.engine)
		self.session=Session()
		self.createTable()	
		try:
			self.init_tags()
		except:
			#logging some tag already exitst !
			TTLog.logger.info("some tag already exist !")
			self.session.rollback()
			pass
	def createTable(self):
		metadata = MetaData()
		rst_table = Table('re_songs_tags',metadata,
		Column('id',Integer,primary_key=True),
		Column('sid',Integer,nullable = False,unique=True),
		Column('title',String(500),nullable = False),
		Column('artist',String(100),nullable = False),
		Column('tag_id',Integer,nullable = False)
		)
		tagid_tag = Table('local_tag_id',metadata,
		Column('local_tag_id',Integer,primary_key = True,nullable = False),
		Column('local_tag_name',String(100),nullable = False)
		)
		metadata.create_all(self.engine)
	def init_tags(self):
		tag_list = [Tag(1,"热歌"),Tag(2,"新歌"),Tag(3,"经典"),Tag(4,"网络"),Tag(5,"影视"),Tag(6,"90年代"),Tag(7,"80年代"),Tag(8,"70年代"),Tag(9,"华语"),
		Tag(10,"粤语"),Tag(11,"欧美"),Tag(12,"日韩"),Tag(13,"伤感"),Tag(14,"寂寞"),Tag(15,"恋爱ING"),Tag(16,"DJ"),Tag(17,"轻音乐"),Tag(18,"钢琴曲"),Tag(19,"中国风"),
		Tag(20,"咖啡屋"),Tag(21,"起床"),Tag(22,"用餐"),Tag(23,"途中"),Tag(24,"学习"),Tag(25,"休闲"),Tag(26,"睡前"),Tag(27,"喜悦"),Tag(28,"放松"),Tag(29,"激动"),
		Tag(30,"日语"),Tag(31,"韩语"),Tag(32,"摇滚"),Tag(33,"乡村"),Tag(34,"R&B"),Tag(35,"古典"),Tag(36,"爵士"),Tag(37,"电子"),Tag(38,"蓝调"),Tag(39,"说唱"),
		Tag(40,"儿歌"),Tag(41,"动漫")]
		self.session.add_all(tag_list)
		self.session.commit()
		
if __name__ == "__main__":
	db = DBHelper()
	#print Song.__table__
	#print Song.__mapper__
#	db.createTable()
#	from sqlalchemy.orm import mapper
#	metadata = MetaData(db.engine)
#	table = Table('re_songs_tags',metadata,autoload=True)
#	print table.columns
#	mapper(Song,table)
#	song = Song(1,'我的歌声里','去玩婷',1)
#	insert = table.insert().execute(sid=song.sid,title=song.title,artist=song.artist,tag=song.tag)
#	try:
#		db.session.add(song)
#		db.session.commit()
#	except:
#		print "something error!"	
