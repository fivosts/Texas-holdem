WORKSPACE=.
LIBS=libs
SRC=src
CC=g++
CFLAGS = -Wall -Wextra -I $(WORKSPACE)/$(LIBS) -I $(WORKSPACE)/$(SRC)


poker_api: main.o api.o game.o poker_player.o poker_dealer.o db_communicator.o
	$(CC) -lsqlite3 -o poker_api.so main.o api.o game.o poker_player.o poker_dealer.o db_communicator.o

main.o: $(WORKSPACE)/$(SRC)/main.cpp
	$(CC) -c $(WORKSPACE)/$(SRC)/main.cpp $(CFLAGS)

api.o: $(WORKSPACE)/$(SRC)/api.cpp
	$(CC) -c $(WORKSPACE)/$(SRC)/api.cpp $(CFLAGS)

game.o: $(WORKSPACE)/$(SRC)/game.cpp
	$(CC) -c $(WORKSPACE)/$(SRC)/game.cpp $(CFLAGS)

poker_player.o: $(WORKSPACE)/$(SRC)/poker_player.cpp
	$(CC) -c $(WORKSPACE)/$(SRC)/poker_player.cpp $(CFLAGS)

poker_dealer.o: $(WORKSPACE)/$(SRC)/poker_dealer.cpp
	$(CC) -c $(WORKSPACE)/$(SRC)/poker_dealer.cpp $(CFLAGS)

db_communicator.o: $(WORKSPACE)/$(SRC)/db_communicator.cpp
	$(CC) -c $(WORKSPACE)/$(SRC)/db_communicator.cpp $(CFLAGS)


# read_file.o: $(WORKSPACE)/$(SRC)/read_file.cpp
# 	$(CC) -c $(WORKSPACE)/$(SRC)/read_file.cpp $(CFLAGS)

clean:
	rm ./*.o