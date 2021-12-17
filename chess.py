import json
import pprint
import requests
import argparse
import os
import random

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

def arena_players(url):
	r = requests.get(url)
	return r.json()['players']

# Construct an argument parser
all_args = argparse.ArgumentParser()

# Add arguments to the parser
all_args.add_argument("-u", "--username", required=False, help="chess.com username")
all_args.add_argument("-t", "--tournament", required=False, help="tournament ID (ex: poulet-1484723)")
all_args.add_argument("-a", "--archives", action='store_true', default=False, required=False, help="game archives")
all_args.add_argument("-s", "--stats", action='store_true', default=False, required=False, help="user stats")
all_args.add_argument("-r", "--random", action='store_true', default=False, required=False, help="Choose a random user among tournament list")
args = vars(all_args.parse_args())

#ARCHIVE ENDPOINT USED FOR API REQUESTS
#https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive-list
ARCHIVE_ENDPOINT='https://api.chess.com/pub/player/{}/games/archives'.format(args['username'])
STATS_ENDPOINT='https://api.chess.com/pub/player/{}/stats'.format(args['username'])
ARENA_ENDPOINT='https://api.chess.com/pub/tournament/{}/1'.format(args['tournament'])

def archives():
	login_file = args['username'] + ".pgn"
	if os.path.exists(login_file):
		os.remove(login_file)
	l = open(login_file, "x")
	for url in archived_games(ARCHIVE_ENDPOINT):
		chess_file = "ChessCom_" + args['username'] + "_" + url[-7:].replace("/", "") + ".pgn"
		if os.path.exists(chess_file):
			os.remove(chess_file)
		f = open(chess_file, "x")
		for games in monthly_games(url):
			f.write(games['pgn'])
			l.write(games['pgn'])
		f.close()
	l.close()

def stats():
	print(user_stats(STATS_ENDPOINT))

def arena_ranking():
	return sorted(arena_players(ARENA_ENDPOINT), key=lambda x : x['points'], reverse=True)

def arena_top_3():
	print(arena_ranking()[0:3])

def arena_random_winner():
	print(random.choice(arena_ranking())['username'])

if args['archives']:
	archives()
elif args['stats']:
	stats()
elif (args['tournament'] and not args['random']):
	arena_top_3()
elif args['random']:
	arena_random_winner()
else:
	all_args.print_help()
