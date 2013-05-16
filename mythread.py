#!/usr/bin/env python
import threading
from fmcrawler import FMCrawler


class  MyThread(threading.Thread):
	def __init__(self,name,data):
		threading.Thread.__init__(self)
		self.t_name = name
		self.t_data = data
	
	def run(self):
		fm = FMCrawler()
		fm.crawl(self.t_data)


if __name__ == "__main__":
	dict_7_9_17_18 = {7:{"4":60050,"1000354":1452},9:{"1":8409},17:{"9":7176},18:{"1000748":32,"1001061":281}}
	dict_3_5_6 = {3:{"1002588":57,"1002453":500,"1000392":157},5:{"10":9000},6:{"5":5500}}
	dict_8_10_11 = {8:{"3":5982},10:{"6":8900},11:{"2":9225}}	
	dict_4_12_13  = {4:{"1000191":273},12:{"17":10000,"18":4578},13:{"77":2336,"1001113":583,"1001571":625}}
	dict_14_15_16 = {14:{"1001105":90,"1000045":96,"1003950":417},15:{"1000606":926,"1000742":379,"1001203":544},16:{"1000106":778,"1001631":115,"1000271":80}}
	dict_20_21_22 = {20:{"32":3460},21:{"1002503":126,"1001621":618},22:{"13":7497,"1000150":305,"32":3460}}
	dict_23_24_25 = {23:{"10":9539,"1002048":418,"1000395":437,"1001975":421},24:{"1001312":292},25:{"1001132":149,"1001351":379}}
	dict_26_27_28 = {26:{"1003413":80,"1002626":63,"1001733":739},27:{"1003687":245},28:{"22":3329,"1000537":30,"1001403":730}}
	dict_29_30_31 = {29:{"1001225":44,"1004219":425},30:{"17":10000},31:{"18":4578}}
	dict_32_33_34 = {32:{"7":8930},33:{"1001433":87,"1002923":34},34:{"16":7122}}
	dict_35_36_37 = {35:{"27":4189},36:{"13":7497,"1000150":305,"1000888":49},37:{"14":9682,"1003159":454}}
	dict_38_39_40 = {38:{"1004179":368,"1000690":60},39:{"15":8403},40:{"1001544":120,"1001678":79,"1001240":130}}
	dict_19_41    = {19:{"1000401":238},41:{"28":5746}}
	


	thread_3_5_6 = MyThread("3_5_6",dict_3_5_6)
	thread_8_10_11 = MyThread("8_10_11",dict_8_10_11)	
	thread_7_9_17_18 = MyThread("7_9_17_18",dict_7_9_17_18)
	
	thread_3_5_6.start()
	thread_8_10_11.start()
	thread_7_9_17_18.start()

	
	thread_3_5_6.join()
	thread_8_10_11.join()
	thread_7_9_17_18.join()