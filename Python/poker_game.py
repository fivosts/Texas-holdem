#!/usr/bin/python2

import argparse, sys
import zmq
import random
# from utilities import *

# parser = argparse.ArgumentParser(description='zeromq server/client')
# parser.add_argument('--bar')
# args = parser.parse_args()

# if args.bar:
#     # client
#     print 'I am client!'
#     context = zmq.Context()
#     socket = context.socket(zmq.REQ)
#     socket.connect('tcp://127.0.0.1:5555')
#     socket.send(args.bar)
#     msg = socket.recv()
#     print msg
# else:
#     # server
#     print 'I am server!'
#     context = zmq.Context()
#     socket = context.socket(zmq.REP)
#     socket.bind('tcp://127.0.0.1:5555')
#     while True:
#         msg = socket.recv()
#         print msg
#         if msg == 'zeromq':
#             socket.send('ah ha!')
#         else:
#             socket.send('...nah')

def define_winner(players):

	# winning_hands = ['four_of_a_kind', 'full_house', 'straight', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']
	

	players_sum = [[] for i in range(0, len(players))]
	winning_combo = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(0, len(players))]

	for player, player_sum in zip(players, players_sum):
		for element in player:
			if element == 'd':
				player_sum.append(10)
			elif element == 'j':
				player_sum.append(11)
			elif element == 'q':
				player_sum.append(12)
			elif element == 'k':
				player_sum.append(13)
			elif element == 'a':
				player_sum.append(14)
			else:
				player_sum.append(int(element))

	for player in players_sum:
		player.sort()

	for player, win_player in zip(players_sum, winning_combo):
		for element in player:
			print element
			win_player[element - 2] += 1
		print win_player

		





	return
	# winning_hands

def poker_training(players):

	list1 = ['2', '3', '4', '5', '6', '7', '8', '9', 'd', 'j', 'q', 'k', 'a']
	deck = list1 + list1 + list1 + list1

	# print deck
	random.shuffle(deck)
	# print deck

	players  = [[] for i in range(0, players)]

	# print players

	count = 0
	flop = []
	turn = []
	river = []
	player_total = []

	for i in range(0,2):
		for player in players:
			player.append(deck[count])
			count += 1
	for i in range(0,3):
		flop.append(deck[count])
		count += 1
	turn.append(deck[count])
	count += 1
	river.append(deck[count])
	count += 1

	print deck
	print players
	print flop
	print turn
	print river
	for player in players:
		player_total.append(player+flop+turn+river)
	print player_total
	winner = define_winner(player_total)

	return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = 'zeromq server/client')
    parser.add_argument('-p', '--players', type = int, help = 'Number of players to train the database')
    args = parser.parse_args()

    if (args.players < 2) or (args.players > 23):
    	print 'invalid number of players'
    	sys.exit(1)

    poker_training(args.players)

    sys.exit(0)