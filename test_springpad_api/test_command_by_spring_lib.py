from spring import Client
from oauth import oauth

consumer_key = "41a9a847fec84370aae6f14f372484fb"
consumer_secret = "7047f8cfee4145968be2e61b30053baa"
access_token = oauth.OAuthToken.from_string(open("oauth_access_token.txt").read())

c = Client(consumer_key, consumer_secret, access_token)
userinfo = c.get_user('me')
#print userinfo['shard']
nuid = c.new_uuid()
c.execute_commands([
	['create', 'Note', '/UUID(%s)/' % nuid],
	['set', '/UUID(%s)/' % nuid, 'name', 'test note'],
	['set', '/UUID(%s)/' % nuid, 'url', 'http://www.baidu.com'],
	['set', '/UUID(%s)/' % nuid, 'text', 'blah blah blah'],
])
