import json
import pprint
import requests
import argparse

'''
HTTP Responses from Chess.com
200 = "enjoy your JSON"
301 = if the URL you requested is bad, but we know where it should be; your client should remember and correct this to use the new URL in future requests
304 = if your client supports "ETag/If-None-Match" or "Last-Modified/If-Modified-Since" caching headers and the data have not changed since the last request
404 = we try to tell you if the URL is malformed or the data requested is just not available (e.g., a username for a user that does not exist)
410 = we know for certain that no data will ever be available at the URL you requested; your client should not request this URL again
429 = we are refusing to interpret your request due to rate limits; see "Rate Limiting" above
'''

def archived_games(url):
	r = requests.get(url)
	return r.json()['archives']

def monthly_games(url):
	r = requests.get(url)
	return r.json()['games']

def user_stats(url):
	r = requests.get(url)
	return r.json()

# Construct an argument parser
all_args = argparse.ArgumentParser()

# Add arguments to the parser
all_args.add_argument("username")
all_args.add_argument("-a", "--archives", action='store_true', default=False, required=False, help="game archives")
all_args.add_argument("-s", "--stats", action='store_true', default=False, required=False, help="user stats")
args = vars(all_args.parse_args())

#ARCHIVE ENDPOINT USED FOR API REQUESTS
#https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive-list
ARCHIVE_ENDPOINT='https://api.chess.com/pub/player/{}/games/archives'.format(args['username'])
STATS_ENDPOINT='https://api.chess.com/pub/player/{}/stats'.format(args['username'])

def archives():
	for url in archived_games(ARCHIVE_ENDPOINT):
		for games in monthly_games(url):
			print(games['pgn'])

def stats():
	print(user_stats(STATS_ENDPOINT))

if args['archives']:
	archives()
elif args['stats']:
	stats()
else:
	all_args.print_help()
