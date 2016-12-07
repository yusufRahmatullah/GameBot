#! /user/bin/python

import json
import requests
import url
import post_data

class Main():
	def __init__(self, username, password, debug=False):
         self.username = username
         self.password = password
         self.debug = debug
		
	def login(self):
         self.r = requests.post(url.login, data=post_data.login(), 
                                headers=post_data.headers())
         self.cookies = self.r.cookies
         if self.debug:
             print("status:{}".format(r.status_code))
     
    def team_set(self, team_name, city_name):
        if self.cookies:
            request.post(url.team_settings, data=post_data.team_settings())

if __name__ == '__main__':
	with open('config.json', 'r') as f:
		config = json.read(f)
	username = config['username']
	password = config['password']
	m = Main(username, password);
	m.login()
