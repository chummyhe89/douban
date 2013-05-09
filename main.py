#!/usr/bin/env python
#coding=utf-8
#author:andy
#date:2013-05-08
import random
from db import DBHelper
from song import Song
from douban import DoubanProtocol

#dataDict={"华语":{"1":100},"八零":{"4":10,"1000354":10}}
dataDict = {18:{"1000748":32,"1001061":281}}
#dataDict={7:{"4":20,"1000354":10},9:{"1":20},17:{"9":20},18:{"1000748":32,"1001061":281}}

class FMCrawler():
	
	def __init__(self):
		self.m_dbPro=DoubanProtocol()	
		self.m_sids=[]
		self.db	= DBHelper()
	
	def crawl(self,data):
		for i in data.keys():
			tag = i
			channels=data[i]
			for j in channels.keys():
				k = 0
				c = 0
				count = channels[j]
				while(k <= 10000 ):
					k+=1
					if(len(self.m_sids) != 0):
						t_sid = self.m_sids[random.randint(0,len(self.m_sids)-1)] 
						jslist = self.m_dbPro.getNewPlayList(j,sid=t_sid)
					else:
						jslist=self.m_dbPro.getNewPlayList(j)
					if len(jslist) != 0:
						songs=self.parseSong(jslist,tag)
				#		print songs
						new_add = self.save_to_DB(songs)
						c+=new_add		
					if count and c>=count:
						break
	def parseSong(self,list,tag):
		if len(list) == 0 :
			return []
		else:
			self.m_sids = []
			songs = []
			for i in range(len(list)): 
				sid=list[i].get('sid')
				title=list[i].get('title')
				artist=list[i].get('artist')
				self.m_sids.append(sid)
				song = Song(sid,title,artist,tag)
				songs.append(song)
			return songs
				
	def save_to_DB(self,songlist):
		if len(songlist) == 0:
			return 0
		else:
			c = 0
			for i in songlist:
				
				try:
					self.db.session.add(i)
					self.db.session.commit()
					c+=1
				except Exception,e:
					#logging
#					print e
					self.db.session.rollback()				
					continue
			return c
if __name__ == "__main__":
	fmCrawler = FMCrawler()
	fmCrawler.crawl(dataDict)
