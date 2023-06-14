## 0x0A. Prime Game
Maria and Ben are playing a game. Given a set of consecutive integers starting from  up to and including , they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play  rounds of the game, where  may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

* Prototype: 
* where  is the number of rounds and  is an array of 
* Return: name of the player that won the most rounds
* If the winner cannot be determined, return 
* You can assume  and  will not be larger than 10000
* You cannot import any packages in this task

Example:

*  = ,  = 

First round: 

* Maria picks 2 and removes 2, 4, leaving 1, 3
* Ben picks 3 and removes 3, leaving 1
* Ben wins because there are no prime numbers left for Maria to choose

Second round: 

* Maria picks 2 and removes 2, 4, leaving 1, 3, 5
* Ben picks 3 and removes 3, leaving 1, 5
* Maria picks 5 and removes 5, leaving 1
* Maria wins because there are no prime numbers left for Ben to choose

Third round: 

* Ben wins because there are no prime numbers for Maria to choose

**Result: Ben has the most wins**
