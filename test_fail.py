#in this case are tests suppose to fail
#we check the failed cases, to make sure the software fails softly.
#no python message should be pop-up
import pytest
from main import *

#keep this function in case we want to add input values share between everyone.
@pytest.fixture
def input_value(): #keep this fixture for future use, incase any fixture is necessary
    return

#should fail to check if computer choices are valid
def test_method1():
    assert get_cpu_choice() not in all_usrchoice

#should fail to check functions for the tie situation
@pytest.mark.parametrize("x,y",[('r','r'),('s','s'),('p','p'),('R','R')])
def test_method2(x,y):
    assert print_winning_mesg(x,y) ==0 #print_winning_mesg not suppose to say you won
    assert find_winner(x,y) not in status #fail to return acceptable status
    assert find_winner(x,y) == 1 #status is 1 for winner, this should fail

#should fail to check functions if user won, because it did ot run and should not be a wimming message.
@pytest.mark.parametrize("x,y",[('r','s'),('s','p'),('p','r')])
def test_method3(x,y):
    assert print_winning_mesg(x,y) ==1 #fail to print you won
    assert find_winner(x,y) == 2 # fail to find the winder flag in find_winner

#should fail to check functions work fine if the user was lost.
@pytest.mark.parametrize("x,y",[('s','r'),('p','s'),('r','p')])
def test_method4(x,y):
    assert find_winner(x,y) == 0 #wrong flag, the wining flag in find_winner

#should fail to check if wrong input sneaked to the system.
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
