#Here are the tests suppose to fail
#we check the failed cases, to make sure the software fails softly.
#no python error message should be poped-up
import pytest
from main import *

#keep this function in case we want to add input values share between everyone.
@pytest.fixture
def input_value(): #keep this fixture for future use, incase any fixture is necessary
    return

#should fail if computer choices are invalid
def test_method1():
    assert get_cpu_choice() not in all_usrchoice

#should fail if functions return invalid flags for the tie situation
@pytest.mark.parametrize("x,y",[('r','r'),('s','s'),('p','p'),('R','R')])
def test_method2(x,y):
    assert print_winning_mesg(x,y) ==0 #print_winning_mesg not suppose to say you won
    assert find_winner(x,y) not in status #fail to return acceptable status
    assert find_winner(x,y) == 1 #status is 1 for winner, this should fail

#should fail functions when the user is winner.  The return flag and message should not be a winning message.
@pytest.mark.parametrize("x,y",[('r','s'),('s','p'),('p','r')])
def test_method3(x,y):
    assert print_winning_mesg(x,y) ==1 #fail to print you won
    assert find_winner(x,y) == 2 # fail to find the winder flag in find_winner

#should fail  if the user lost, but the flag is for the winner.
@pytest.mark.parametrize("x,y",[('s','r'),('p','s'),('r','p')])
def test_method4(x,y):
    assert find_winner(x,y) == 0 #wrong flag, the wining flag in find_winner

#should fail if wrong input sneaked to the system.
@pytest.mark.parametrize("x,y",[('A','a'),('p','k'),('1','2')])
def test_method5(x,y):
    assert print_winning_mesg(x, y) ==1 #wrong charachters caught
    assert find_winner(x,y) == 1

#to_do: make another funtion for special charachters , ...
invalid_chars = ['*', '/', '+']
def test_invalid_char():
    #with pytest.raises(Exception) as exp:
    #    print_winning_mesg(x.y)
    #assert str(exp.value) == " Message"
    pass
if __name__ == '__main__':
        pytest.main()
