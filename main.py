"""
main.py:    Play a game of rock, paper, scissors

Game Description: Rock, Paper, Scissors
Human Plays Rock, Paper, Scissors game against the computer.
The winner is decided by these rules:

* Rock blunts scissors
* Paper covers rock
* Scissors cut paper

Process
- First, let the player choose Rock, Paper or Scissors by typing the letter ‘r’, ‘p’ or ‘s’;
- Then computers turn;
- Decide game win, lose or draw, print choice of both sides

options: 'r' or 'p' or 's'

Arguments (for future implmentation): - Suggestion to add an option if the players wants to continue the play
            so in future we can as the user to say yes to continue the game.
            - ask if the user want to quit by typing q
"""

import random
import sys

#defining global variable here
#we seperate human choice in case we wanted to add more options to human choice.
all_usrchoice = 'rps'
#later add lizard and spock to the cpu choices
cpu_all_choices = 'rps'
#we can add lizard spock
dictchoice= {'s':'scissors', 'r':'rock', 'p':'paper'} #use this dictionaly to print the choices
status = [0,1,2,3] # variable for debugging: didnot pick choice (quitting) =0 , winning = 1, tie = 2, losing= 3
#This function get the player choice. If the choice is not acceptable, too bad, we quit.
def ask_usrchoice():
    userinput = None
    #we may want to add a while loop for repeating the game
    if userinput is None:
        try:
            userinput = input('Please select a choice, What do you choose?\nr for rock, p for paper, s for scissors:')
            if not userinput:
                raise ValueError('empty string')
        except ValueError:
            print("\nyou did not provide any input, quitting")
            sys.exit(0)
        #to_do: seperate this part in a function call and test is by pytest:
        #this case also should be an exception
        if userinput.lower() not in all_usrchoice: #user enters wrong choice
            print("Your choice:", userinput, "is not an option, quitting the game")
            quit(0)
    return userinput.lower()
#getting random choice
def get_cpu_choice():
    #get a random number between 1 to 3
    cpu_random_choice = random.randint(1, 3)
    cpu_choice = cpu_all_choices[cpu_random_choice -1]
    return cpu_choice

#this funtion should print winning message, but what if accidently other functions abuse it?
#then let make it testable...
def print_winning_mesg(userinput, cpu_choice):
    #here we should raise an expception
    if userinput and cpu_choice not in all_usrchoice: #this should neve happens, for debugging purpose only
        #to_do
        """if not isinstance(userinput, str):
            raise ValueError("userinput must be a string")"""
        return 1 #use the return flag to debug and test the function
    elif userinput== cpu_choice: #Tie user should not come here, just double checking
        return 1
    else:
        print("Yes, You won!")
        print('%s wins over %s' % (dictchoice[userinput], dictchoice[cpu_choice]))
        return 0 #flag 0 means the function passed the test.

def find_winner(userinput, cpu_choice):
    #print the message tie, win or lose
    #use the status and flag for debuggging purpose. status here: winning = 1, tie = 2, losing= 3
    if userinput and cpu_choice not in all_usrchoice: #this should neve happens, for debugging purpose only
        #to_do
        """if not isinstance(userinput, str):
            raise ValueError("user input must be a string")"""
        return 100
    elif userinput == cpu_choice: #for tie status
        print("Tie game, You and computer won!")
        flag = status[2]
    elif userinput == 'r' and cpu_choice == 's': #Yes, user wins, status 1
        print_winning_mesg(userinput, cpu_choice)
        flag = status[1]
    elif userinput == 's' and cpu_choice == 'p': #Yes, user wins, status 1
        print_winning_mesg(userinput, cpu_choice)
        flag = status[1]
    elif userinput == 'p' and cpu_choice == 'r': #Yes, user wins, status 1
        print_winning_mesg(userinput, cpu_choice)
        flag = status[1]
    else:
        print('This time you lose.') #user lost, status 3
        print('%s wins over %s' % (dictchoice[cpu_choice], dictchoice[userinput]))
        flag  = status[3]
    return flag #we use this flag for testig.


def game_start():
    #we could have a choice for the user to play multiple times, by adding a while loop.
    print("Welcome to the fantastic game of rock, paper, scissors.")
    userinput = ask_usrchoice()
    cpu_choice = get_cpu_choice()
    print("player choice:", dictchoice[userinput] )
    print("computer choice:", dictchoice[cpu_choice])
    result = find_winner(userinput, cpu_choice)
    return result #use the results for debugging purpose

if __name__ == "__main__":
    #here we can ask user if she wants to play mutiple times.
    #if yes, we can call os.system('game.py') in a while loop
    #Also, for repeating game, we can have os.system("cls") to clear the screen
    game_start()
