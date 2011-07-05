import oauth2 as oauth
import httplib2

CONSUMER_KEY = "41a9a847fec84370aae6f14f372484fb"
CONSUMER_PRIVATE = "7047f8cfee4145968be2e61b30053baa"

def save_request_token(tk):
	f = open("oauth_request_token.txt", "w")
	f.write(tk)
	f.close()

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_PRIVATE)
request = oauth.Request.from_consumer_and_token(consumer, token=None, http_url="http://springpadit.com/api/oauth-request-token", http_method='GET')
signature_method = oauth.SignatureMethod_HMAC_SHA1()
request.sign_request(signature_method, consumer, None)
url = request.to_url()
response, data = httplib2.Http().request(url)
save_request_token(data)
request_token = oauth.Token.from_string(data)
#print "Request Token: %s" % request_token
url = 'http://springpadit.com/api/oauth-authorize?%s' % request_token
print "Access url: %s" % url
