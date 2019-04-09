import click

import requests

class BreachedPassword(object):
	def __init__(self, url, headers):
		self.url = url
		self.headers = headers
		
	def _get(self):
		#TODO:
		response = requests.get(self.url, headers = self.headers)
		
	def check_passwd_breach(self, passwd):
		#TODO:
		self.passwd = passwd
		print "This is your passwd: {0}".format(passwd)
