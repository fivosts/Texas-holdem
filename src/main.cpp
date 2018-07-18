#include "api.h"
#include "classes.h"
#include <iostream>
#include <chrono>

#define BENCHMARK_IT 100

extern std::map<unsigned int, std::string> card_values;

int main(){

	unsigned int players;

	std::cout << "Select number of players" << std::endl;
	std::cin >> players;
	if ((players < 2) || (players > 20)){
		std::cout << "Invalid number of players" << std::endl;
		return 1;
	}

	db_communicator *database = new db_communicator(players);
	game *poker_game = new game(players);

	// while(1){
    std::chrono::high_resolution_clock::time_point t1 = std::chrono::high_resolution_clock::now();

    for (unsigned int i = 0; i < BENCHMARK_IT; i++){
		poker_game->play_round();
		database->store_to_db(poker_game);
		poker_game->reset_round();    	
    }

    std::chrono::high_resolution_clock::time_point t2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2-t1);
    std::cout << time_span.count() << " seconds" << std::endl << "Average time per iteration: " << (1000 * time_span.count()) / BENCHMARK_IT << "ms" << std::endl;


	// }

	delete database;

	exit(0);
}