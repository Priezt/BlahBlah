import oauth2 as oauth
import httplib2
import json

def load_access_token():
	f = open("oauth_access_token.txt")
	tk = f.read()
	f.close()
	access_token = oauth.Token.from_string(tk)
	return access_token

CONSUMER_KEY = "41a9a847fec84370aae6f14f372484fb"
CONSUMER_PRIVATE = "7047f8cfee4145968be2e61b30053baa"
access_token = load_access_token()
print "access token: %s" % access_token

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_PRIVATE)
request = oauth.Request.from_consumer_and_token(consumer, token=access_token, http_url="http://springpadit.com/api/users/vegetabird@gmail.com", http_method='GET')
signature_method = oauth.SignatureMethod_HMAC_SHA1()
request.sign_request(signature_method, consumer, access_token)
url = request.to_url()
print "request url: %s" % url
response, data = httplib2.Http().request(url)
print "data:"
print data
#userinfo = json.loads(data)
f = open("user_info.txt", "w")
f.write(data)
f.close()
