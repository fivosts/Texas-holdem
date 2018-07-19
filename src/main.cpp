#include "api.h"
#include "classes.h"
#include <iostream>
#include <unistd.h>
#include <errno.h>
#include <chrono>
#include <signal.h>
#include <sys/mman.h>

// #define BENCHMARK_IT 100

volatile sig_atomic_t flag = 0;
static unsigned int db_counter = 2;
extern std::map<unsigned int, std::string> card_values;

void signal_catcher(int sig){

	flag = 1;
	return;
}

void train_db(unsigned int players){

	if(flag){ 
		std::cout << "Poutsa" << std::endl; return; }

	db_communicator *database = new db_communicator(players);
	game *poker_game = new game(players);

	while(!flag){
    // std::chrono::high_resolution_clock::time_point t1 = std::chrono::high_resolution_clock::now();

		poker_game->play_round();
		database->store_to_db(poker_game);
		poker_game->reset_round();    	

    // std::chrono::high_resolution_clock::time_point t2 = std::chrono::high_resolution_clock::now();
    // std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2-t1);
    // std::cout << time_span.count() << " seconds" << std::endl << "Average time per iteration: " << (1000 * time_span.count()) / BENCHMARK_IT << "ms" << std::endl;
	}
	delete database;
	return;
}

void training_process_daemon(unsigned int* &pid){

	int p = fork();

	if (p == -1){ perror("Fork failure: "); }

	else if (p == 0){
	
		train_db(db_counter);
		pid[db_counter - 2] = 0;
		exit(0);
	}

	else{

		pid[db_counter - 2] = p;
		db_counter++;
		if ((db_counter < 21) && (!flag)){
			usleep(300000);
			training_process_daemon(pid);
		}
	}

	return;
}

int main(int argc, char** argv){

	signal(SIGINT, signal_catcher);

	unsigned int *pid_list = (unsigned int*)mmap(NULL, 19 * sizeof(unsigned int), PROT_READ|PROT_WRITE, MAP_ANON|MAP_SHARED, -1, 0);

	training_process_daemon(pid_list);

	sleep(1);

	std::cout << "Woken up " << db_counter - 2 << " processes successfully" << std::endl;

	while(!flag){}

	for(unsigned int i = 0; i < db_counter; i++){
		kill(pid_list[i], 2);
	}

	std::cout << std::endl << "Waiting for processes to terminate..." << std::endl;

	while([](unsigned int* &pid_list, unsigned int &db_counter){
		unsigned int sum = 0;
		for (unsigned int i = 0; i < db_counter; i++){
			sum += pid_list[i];
		}
		return sum;
	}(pid_list, db_counter)){}

	std::cout << "Program terminated successfully" << std::endl;

	exit(0);
}