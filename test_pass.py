#in this case are tests suppose to pass
import pytest
from main import *

#keep this function in case we want to add input values share between everyone.
@pytest.fixture
def input_value(): #keep this fixture for future use, incase any fixture is necessary
    pass_cases = 'rps'
    return

#check if computer choices are valid
def test_method1():
    assert get_cpu_choice() in all_usrchoice

#check functions for the tie situation
@pytest.mark.parametrize("x,y",[('r','r'),('s','s'),('p','p')])
def test_method2(x,y):
    assert print_winning_mesg(x,y) ==1 #print_winning_mesg not suppose to say you won
    assert find_winner(x,y) in status #check if funtion return acceptable status
    assert find_winner(x,y) == 2 #status is 2 for tie

#check functions if user won.
@pytest.mark.parametrize("x,y",[('r','s'),('s','p'),('p','r')])
def test_method3(x,y):
    assert print_winning_mesg(x,y) ==0 #print function should print you won
    assert find_winner(x, y) in status #find_winner should return acceptable status
    assert find_winner(x,y) == 1 #the wining flag in find_winner

#check functions work fine if the user was lost.
@pytest.mark.parametrize("x,y",[('s','r'),('p','s'),('r','p')])
def test_method4(x,y):
    assert find_winner(x, y) in status #find_winner should return acceptable status
    assert find_winner(x,y) == 3 #the loser flag in find_winner

#check if wrong input sneaked to the system.
#may consider re for using specail charachter: re.compile(r"[\\/]+")
@pytest.mark.parametrize("x,y",[('A','a'),('p','k'),('1','2')])
def test_method5(x,y):
    assert print_winning_mesg(x, y) ==1 #wrong charachters caught
    assert find_winner(x,y) == 100

if __name__ == '__main__':
        pytest.main()
