#ifndef __CLASSES_H__
#define __CLASSES_H__
#include "api.h"
#include "sqlite3.h"

class poker_player{

public:
	poker_player(){}
	~poker_player(){}

	void draw_hand(const card &first_card, const card &second_card);
	void reset_round();
	void print_state() const;
	inline void set_win_state(bool state){
		winner = state;
		return;
	}
	inline unsigned int get_hand_combo() const{
		return hand_combination;
	}
	inline std::vector<int> get_high_cards() const{
		// return std::move(high_cards);
		return high_cards;
	}
	inline const std::vector<card> & get_hand() const{
		return hand;
	}
	inline bool is_winner() const{
		return winner;
	}

	friend void poker_comb_finder(poker_player &player, const poker_dealer &dealer);

private:
	std::vector<card> hand;
	bool winner;
	unsigned int hand_combination;
	std::vector<int> high_cards;
};

class poker_dealer{

public:
	poker_dealer(){}
	~poker_dealer(){}

	void draw_table(const card *flop_pointer);
	void reset_round();
	void print_state() const;
	inline const std::vector<card> & get_flop() const{
		return flop;
	}
	inline card get_turn() const{
		return turn;
	}
	inline card get_river() const{
		return river;
	}
	friend void poker_comb_finder(poker_player &player, const poker_dealer &dealer);

private:
	std::vector<card> flop;
	card turn;
	card river;
};

class game{

public:
	game(unsigned int players);
	~game(){
		delete [] player_list;
		delete [] dealer;
	}

	void play_round();
	void reset_round();
	void print_deck() const;
	void print_state() const;

	friend class db_communicator;

private:
	card deck[4*13];
	poker_player *player_list;
	poker_dealer *dealer;
	unsigned int player_number;
};

class db_communicator{

public:

	db_communicator(unsigned int players);
	~db_communicator();
	void store_to_db(const game * const &poker_game);

private:

	bool prepare_stage_write(const char *command);
	const unsigned char *prepare_stage_read(const char *command);

	sqlite3 *db_conn;
	sqlite3_stmt *db_stmt;
	const char *db_name;
};

#endif