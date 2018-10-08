#!/usr/bin/python2

import sys, os, sqlite3, argparse
from utilities import *

def poker_training(name):

	conn = sqlite3.connect(name)
	cur = conn.cursor()

	hand = ''
	flop = ''
	turn = ''
	river = ''

	while True:
		try:
			hand = get_poker_cards(2)
			hand_id, sorted_hand = sort_string_id(hand)

			flop = get_poker_cards(3)
			flop += hand
			flop_id, sorted_flop = sort_string_id(flop)

			turn = get_poker_cards(1)
			turn += flop
			turn_id, sorted_turn = sort_string_id(turn)

			river = get_poker_cards(1)
			river += turn
			river_id, sorted_river = sort_string_id(river)

			win_flag = 0
			while True:
				win_flag = str(raw_input('Did you win ?\n'))
				if win_flag == 'y' or win_flag == 'Y':
					win_flag = 1
					break
				elif win_flag == 'n' or win_flag == 'N':
					win_flag = 0
					break
				else:
					pass

			cur.execute('SELECT * FROM hand WHERE ID = ?', (hand_id,))	
			if cur.fetchone() == None:
				cur.execute('INSERT INTO hand (ID, Value, Encounters, Wins) ValueS (?, ?, 1, ?)', (hand_id, ''.join(sorted_hand), win_flag))
			else:
				cur.execute('UPDATE hand SET Encounters = Encounters + 1, Wins = Wins + ?', (win_flag,))

			cur.execute('SELECT * FROM flop WHERE ID = ?', (flop_id,))	
			if cur.fetchone() == None:
				cur.execute('INSERT INTO flop (ID, Value, Encounters, Wins) ValueS (?, ?, 1, ?)', (flop_id, ''.join(sorted_flop), win_flag))
			else:
				cur.execute('UPDATE flop SET Encounters = Encounters + 1, Wins = Wins + ?', (win_flag,))

			cur.execute('SELECT * FROM turn WHERE ID = ?', (turn_id,))	
			if cur.fetchone() == None:
				cur.execute('INSERT INTO turn (ID, Value, Encounters, Wins) ValueS (?, ?, 1, ?)', (turn_id, ''.join(sorted_turn), win_flag))
			else:
				cur.execute('UPDATE turn SET Encounters = Encounters + 1, Wins = Wins + ?', (win_flag,))

			cur.execute('SELECT * FROM river WHERE ID = ?', (hand_id,))	
			if cur.fetchone() == None:
				cur.execute('INSERT INTO river (ID, Value, Encounters, Wins) ValueS (?, ?, 1, ?)', (river_id, ''.join(sorted_river), win_flag))
			else:
				cur.execute('UPDATE river SET Encounters = Encounters + 1, Wins = Wins + ?', (win_flag,))

			conn.commit()
		except KeyboardInterrupt:
			break
			
	conn.close()

	return

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description = 'Texas Hold-em predictor')
	Optional_args = parser.add_argument_group('Optional Arguments')
	Optional_args.add_argument('-db', '--database', help = 'path to the history database of playing')
	args = parser.parse_args()

	name = ''

	if args.database == None:

		databases = [file for file in os.listdir('./') if file.split('.')[-1] == 'db']

		if len(databases) == 0:
			while True:
				new = str(raw_input('No databases found. Create new? (y/n)\n'))
				if new == 'y' or new == 'Y':
					name = ''
					while name.split('.')[-1] != 'db' or (len(name.split('.')) != 2):
						name = str(raw_input('Enter a valid database name (example.db): '))
					database_init(name)
					break
				elif new == 'n' or new == 'N':
					print 'Ok, bye'
					sys.exit(0)
				else:
					pass
		else:
			print "Is {0} your database ?".format(str(databases[0]))
			name = str(databases[0])
			# cur.execute("SELECT * FROM poker")
			#todo db confirmation

	poker_training(name)
