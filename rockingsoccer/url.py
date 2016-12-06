#! /user/bin/python

team_settings = 'http://rockingsoccer.com/en/soccer/team_settings'
login = "http://rockingsoccer.com/en/soccer"

post_general_setting = {
	"method" : "POST",
	"Content-Type" : "application/x-www-form-urlencoded"
}
post_login = {
	"username" : "<username>",
	"password" : "<password>",
	"login" : ""
}
post_team_settings = {
	"team_name" : "<team_name>",
	"city_name" : "<city_name>",
	"save" : "Save"
}