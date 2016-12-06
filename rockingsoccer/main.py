#! /user/bin/python

from selenium import webdriver as wd
import json
import url

class Main():
	def __init__(self, username, password):
		self.username = username
		self.password = password
	
	def init(self):
		self.b = wd.Chrome()
		
	def login():
		self.b.get('http://rockingsoccer.com/en/soccer')

if __name__ == '__main__':
	with open('config.json', 'r') as f:
		config = json.read(f)
	username = config['username']
	password = config['password']
	m = Main(username, password);
	m.login()
