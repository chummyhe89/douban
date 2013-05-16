#!/usr/bin/env python

import logging
class TTLog:
	logger = logging.getLogger()
	loghandler = logging.FileHandler('./log.txt')	
	logformatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	loghandler.setFormatter(logformatter)
	logger.addHandler(loghandler)
	logger.setLevel(logging.NOTSET)

if __name__ == '__main__':
	TTLog.logger.info("This is a test case for TTLog")
