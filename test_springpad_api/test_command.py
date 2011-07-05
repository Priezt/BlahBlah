import oauth2 as oauth
import httplib2
from urllib import urlencode
import uuid
import json
import string

def load_access_token():
	f = open("oauth_access_token.txt")
	tk = f.read()
	f.close()
	access_token = oauth.Token.from_string(tk)
	return access_token

def load_user_info():
	f = open("user_info.txt")
	uif = json.loads(f.read())
	f.close()
	return uif

def get_uuid():
	uif = load_user_info()
	result_uid = str(uuid.uuid4())
	result_uid = "/UUID(%s%s%s)/" % (uif['shard'], '3', result_uid[3:])
	print "UUID: %s" % result_uid
	return result_uid

CONSUMER_KEY = "41a9a847fec84370aae6f14f372484fb"
CONSUMER_PRIVATE = "7047f8cfee4145968be2e61b30053baa"
access_token = load_access_token()
print "access token: %s" % access_token
consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_PRIVATE)
request = oauth.Request.from_consumer_and_token(consumer, token=access_token, http_url="http://springpadit.com/api/users/me/commands", http_method='GET')
signature_method = oauth.SignatureMethod_HMAC_SHA1()
request.sign_request(signature_method, consumer, access_token)
url = request.to_url()
print "request url: %s" % url

def do_command(cmd_str):
	print "command str:"
	print cmd_str
	#response, data = httplib2.Http().request(url, "POST", urlencode(cmd_str))
	response, data = httplib2.Http().request(url, method="POST", body=cmd_str, headers={'Content-type': 'application/json; charset=UTF-8', 'X-Spring-Client': 'api-test'})
	print "response data:"
	print data

commands = []
my_uuid = get_uuid()
commands.append("['create','/Type(Note)/','%s']" % (my_uuid))
commands.append("['set','%s','name', 'test note']" % (my_uuid))
#do_command("[%s]" % string.join(commands, ","))
do_command("[['create','/Type(Note)/','%s']]" % (my_uuid))
do_command("[['set','%s','name', 'test note']]" % (my_uuid))
