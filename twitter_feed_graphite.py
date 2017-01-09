#!/usr/bin/env python
import twitter
import socket
from config import config

api = twitter.Api(config['consumer_key'],
                  config['consumer_secret'],
                  config['access_token_key'],
                  config['access_token_secret'],
                  sleep_on_rate_limit=True)

stats = {}

stats['followers'] = len(api.GetFollowers())
stats['friends'] = len(api.GetFriends())
stats['mentions'] = len(api.GetMentions())
stats['retweets'] = len(api.GetRetweetsOfMe())
stats['favorites'] = len(api.GetFavorites())

def send_message(stat_name, value):
    message = config['graphite_api_key'] + "." + stat_name + " %s\n" % value
    print message
    conn = socket.create_connection(("carbon.hostedgraphite.com", 2003))
    conn.send(message)
    conn.close()

for key in stats:
    print(key + ": " + str(stats[key]))
    send_message("personal.twitter." + key, stats[key])
