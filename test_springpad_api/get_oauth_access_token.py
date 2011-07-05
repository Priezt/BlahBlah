import oauth2 as oauth
import httplib2

def load_request_token():
	f = open("oauth_request_token.txt")
	tk = f.read()
	f.close()
	request_token = oauth.Token.from_string(tk)
	return request_token

def save_access_token(tk):
	f = open("oauth_access_token.txt", "w")
	f.write(tk)
	f.close()

CONSUMER_KEY = "41a9a847fec84370aae6f14f372484fb"
CONSUMER_PRIVATE = "7047f8cfee4145968be2e61b30053baa"
request_token = load_request_token()
print "request token: %s" % request_token

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_PRIVATE)
request = oauth.Request.from_consumer_and_token(consumer, token=request_token, http_url="http://springpadit.com/api/oauth-access-token", http_method='GET')
signature_method = oauth.SignatureMethod_HMAC_SHA1()
request.sign_request(signature_method, consumer, request_token)
url = request.to_url()
response, data = httplib2.Http().request(url)
#print "data: %s" % data
access_token = oauth.Token.from_string(data)
print "Access Token: %s" % access_token
save_access_token("%s" % access_token)

