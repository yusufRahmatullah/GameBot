# -*- coding: utf-8 -*-
#! /user/bin/python
"""
Created on Wed Dec 07 09:24:13 2016

@author: E460
"""

def login(username, password):
    post_login = {
    	"username" : "{}".format(username),
    	"password" : "{}".format(password),
    	"login" : ""
    }
    return post_login

def team_settings(team_name, city_name):
    post_team_settings = {
    "team_name" : "{}".format(team_name),
    	"city_name" : "{}".format(city_name),
    	"save" : "Save"
    }
    return post_team_settings

def headers():
    header = {
    "Content-Type" : "application/x-www-form-urlencoded"
    }
    return header
