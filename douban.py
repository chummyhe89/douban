#!/usr/bin/env python
#coding=utf-8
#author:andy
#date:2013-05-08

'''
class for douban request
'''
import random
import urllib
import urllib2
import json
#import adsl
from log import TTLog
import cookielib

class DoubanProtocol:
	'''
	request data from douban fm
	'''
	baseURL = "http://douban.fm/j/mine/playlist"	
	base_header = {'user-Agent':'Mozilla/5.0 (Windows NT 6.1;rv:20.0) Gecko/20100101 firefox/20.0'}
	cookie ='''flag="ok"; ac="1367818273"; bid="Uh/2OSmfpFg"; openExpPan=Y; __utma=58778424.1659846240.1367816694.1368083567.1368087586.10; __utmb=58778424.30.9.1368090923372; __utmc=58778424; __utmz=58778424.1367816378.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3fm; __utmv=58778424.7040; dbcl2="70402429:XCEnVQF8N7o"; fmNlogin="y"; ck="ruWQ"'''
	def __init__(self):
#		self.m_adsl=Adsl()
		pass

	def login(self,user,pw):
		pass
	def get_10_random_chars(self):
		ten_chars = ''
		chars_pool = ['a','b','c','d','e','f','g','h','i','j','k','m','l','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
		for i in range(10):
			ten_chars+=chars_pool[random.randint(0,len(chars_pool)-1)]
		return ten_chars

	def getNewPlayList(self,channel,**sid):
		headers =DoubanProtocol.base_header
		headers['Referer'] = 'http://douban.fm'
		headers['Cookie'] = DoubanProtocol.cookie
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
		urllib2.install_opener(opener)
		if len(sid) == 0:
			songid = ""
			type = "n"
		else:
			songid = str(sid['sid'])
			type = "p"
		params = urllib.urlencode({"type":type,"channel":channel,"from":"radio","r":self.get_10_random_chars(),"sid":songid,"pt":220.0,"pb":64})
		url = DoubanProtocol.baseURL + "?%s" %params
#		print url
		try:
			req = urllib2.urlopen(urllib2.Request(url=url,headers=headers))
		except Exception,e:
			TTLog.logger.error("request failed ! error:"+str(e))
			return []
		if(req.code == 200 ):
			try:
				obj = json.load(req)
			except Exception,e:
				TTLog.logger.error("parse response json str failed!")
				return []
			if obj['r'] != 0:
				TTLog.logger.error("request error!")
				req.close()
				return []
			else:
				return obj['song']
		else:
			TTLog.logger.error("not 2xx response code !")
			#change ip
			return []

if __name__ == "__main__":
	doubanfm = DoubanProtocol()
	newList=doubanfm.getNewPlayList(1)
	print newList
