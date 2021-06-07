#Take home assignment for Maria: Rock, Paper, Scissors

## Description: 
make a Rock, Paper, Scissors game and play against the computer. The game returns the winner by these rules:
      Rock blunts scissors, and Paper covers rock,  Scissors cut paper

#Requirements: Python 3.3 or more, Docker 

## Files in the package:
	There are four files in this package:

         “main.py”: This file includes all functions necessary to implement the game to collect the user input 
	 	  and compare it to the CPU random choice and print the correct information that who is the winner:
		- ask_usrchoice – to get the input from the user.
		- get_cpu_choice - to get a randomized input from CPU.
		- print_winning_mesg – to print the winning messages.
		- find_winner – to check who the user is.
		- game_start – to start the game and call the above functions.

	“test_passy.py”: This file imports pytest includes a different combination of input for the cases 
		that the tests suppose to pass
		- when the user wins
		- when the CPU wins
		- when it is a tie
		- when the  user inputs a string rather than “rps” and the game prints the correct message

	“test_fail.py”: This file imports pytest and every test in this file suppose to fail softly.
		- When it is a tie game, check if invalid message is printed. 
		- When “find_winnner“ returns incorrect status and the “print_winning_mesg”  prints an invalid message
		- Even if the user input is invalid, the game prints the winning message.
		- "to_do" part: I would like to develope a function for invalid charachter input for “print_winning_mesg” 
		   and catch the exceptions.

	“test_patch.py”:  This file mocks user input by “unnitest.mock” :
		- Check the input for the function “ask_userchoice”
		- Check the if correct input is passed to “game_start”
		- “to_do” part: I would like to develop a  test for invalid characters input to the above functions
		    by catching exceptions.

## Development Style: TDD. Each functionality is written so that the function is fully testable against happy or sad input.

## How to play game: Open a development environment like Pycharm or VS. Open all four files in one directory. 
     --run main.py:
	- Enter a choice from ‘rps’. The game prints who won terminates the game.
	- To play another game, run main again
	- If the user inputs nothing, the game will quit.
	- If the user did not read the instruction and put an invalid input, then the game exits.

     --run “test_passy.py”:
	- run this test and the results should show all happy cases.
     --run “test_fail.py”:
	- run this test and the results should show all failed/sad cases. 
     --run “test_patch.py”:
	- run this test to mock userinput for winning/tie/losing cases. 

## To_do: 
	- Develop the game so to play multiple games:  In future, a while loop can be added to the function “game_start” and check if she/he wants to play again.
	- Add exceptions for non-valid string input and test them in the testing files.

## Docker file number 1: 
Here the first Docker file is developed. Herer is the Dockerfile for running main.py and to play the game only. 
For running the tests, a second Docker file is used and another github repository is created (see the related readme.txt).
	
	Commands to run play the game on Docker:
	- “cd” to the folder that the main.py is located.	
	- To build Docker file:  “docker build -t main”
	- To run Docker image:  “docker run -it main”

#Docker file number 2: I made a secondary directory/repository for this project. Please see the other readme.txt for the next Docker project.






