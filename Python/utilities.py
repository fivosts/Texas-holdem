#!/usr/bin/python2

import sys, os, sqlite3

round_id = 0
round_list = ['hand', 'flop', 'turn', 'river']

def sort_string_id(in_string):

	h_id = 0
	str_to_id_list = []

	for it, card in enumerate(in_string):
		if card.isalpha():
			if card == 'j':
				in_string[it] = 'J'
			elif card == 'q':
				in_string[it] = 'Q'
			elif card == 'k':
				in_string[it] = 'K'
			elif card == 'a':
				in_string[it] = 'A'
			elif card == 'd':
				in_string[it] = 'D'

	for card in in_string:
		if card.isalpha():
			if card == 'J':
				str_to_id_list.append(11)
			elif card == 'Q':
				str_to_id_list.append(12)
			elif card == 'K':
				str_to_id_list.append(13)
			elif card == 'A':
				str_to_id_list.append(14)
			elif card == 'D':
				str_to_id_list.append(10)
		else:
			str_to_id_list.append(int(card))

	str_to_id_list, in_string = (list(t) for t in zip(*sorted(zip(str_to_id_list, in_string))))

	for it, key in enumerate(str_to_id_list):
		h_id += (key - 2)*(14**(len(str_to_id_list) - (it + 1)))

	return h_id, in_string

def get_poker_cards(length):

	figures = ['d', 'D', 'j', 'J', 'q', 'Q', 'k', 'K', 'a', 'A']
	global round_id
	round_id = (round_id + 1)%(4)
	
	global round_list

	while True:
		cards = list(raw_input('Insert your {0}\n'.format(round_list[round_id - 1])))
		if len(cards) != length:
			print '{0} is consisted of {1} cards!'.format(round_list[round_id - 1], str(length))
		else:
			invalid = False
			for card in cards:
				if (card.isdigit() == False or card == '1') and (card not in figures):
					print 'Invalid type of card'
					invalid = True
					break
			if invalid == False:
				break
			else:
				invalid = False
	return cards


def database_init(name):

	conn = sqlite3.connect(name)
	cur = conn.cursor()

	cur.execute("CREATE TABLE hand (ID integer, Value text, Encounters integer, Wins integer, PRIMARY KEY (ID))")
	cur.execute("CREATE TABLE flop (ID integer, Value text, Encounters integer, Wins integer, PRIMARY KEY (ID))")
	cur.execute("CREATE TABLE turn (ID integer, Value text, Encounters integer, Wins integer, PRIMARY KEY (ID))")
	cur.execute("CREATE TABLE river (ID integer, Value text, Encounters integer, Wins integer, PRIMARY KEY (ID))")

	conn.commit()
	conn.close()
	return