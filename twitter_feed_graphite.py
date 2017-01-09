#!/usr/bin/env python
import twitter
import socket
from config import config

api = twitter.Api(config['consumer_key'],
                  config['consumer_secret'],
                  config['access_token_key'],
                  config['access_token_secret'])
followers = api.GetFollowers()
follower_count = len(followers)
print(follower_count)

message = config['graphite_api_key'] + ".personal.twitter.followers %s\n" % follower_count

conn = socket.create_connection(("carbon.hostedgraphite.com", 2003))
conn.send(message)
conn.close()
