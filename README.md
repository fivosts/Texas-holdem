I like playing poker now and then, but I am a terrible player because I frequently get overly excited (or bored), go all in and lose. So I decided to make something that will be able to advise me on what to do, given the status of the game (my hand, the flop, the number of players etc.) and hopefully become more successfull at it.

This is a program that plays texas holdem by itself in order to train itself on the probabilities of each given hand. The rules of the game and the deck of the cards are just like in reality. The outcomes of possible combination of cards/players etc. are stored in databases (C++ sqlite module used).

After collecting enough data from game simulation, the program can then receive a hand/flop/turn/river/number of players combination and output the probability of winnning. However, there is no real learning (ML wise) in this program. Only a history of how many times a given combination was encountered and how many of them was this combination victorious.

You may then ask, why did not I just calculate analytically the probability of each poker combination ?

Because:
A) At some point I want to insert a PNN in this implementation and make it use real learning.
B) Because I wanted to get my hands on the C++/python sqlite module and learn how to use it.
C) It was more fun.
D) Why not ?

If you have any good ideas about this project, contact me (fivos_ts@hotmail.com) . Enjoy!
