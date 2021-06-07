#Here I tried to use patch from mock to mock user input for ask_userchoice() funtion
import unittest
from unittest.mock import Mock
from main import *

#setup funtions will be uses for any future setup.
class test_me(unittest.TestCase):
    def setUp(self):
        return

    #the followoing cases should pass with lower case, we are patching the input
    @unittest.mock.patch('builtins.input', create= True)
    def test_1(self, mock_input):
        mock_input.side_effect = 'rps' #checking lowercase and uppercase
        result = ask_usrchoice()
        self.assertEqual(result, 'r')
        result = ask_usrchoice()
        self.assertEqual(result, 'p')
        result = ask_usrchoice()
        self.assertEqual(result, 's')


    #testing game_start()
    @unittest.mock.patch('builtins.input', create= True)
    def test_2(self, mock_input):
        mock_input.side_effect = 'rps'
        result = game_start()
        self.assertIn(result, status)
        result = ask_usrchoice()
        self.assertEqual(result, 'p')
        result = ask_usrchoice()
        self.assertEqual(result, 's')

    #to_do: the follwing test cases should be implemented and an Exception should be caught
    #wrong input (upper and lower), numbers, special charachters patch should raise an exception

    fail_cases1 = ['a','A','x','y', 'X','Y']
    fail_cases2 = ['1','', '.', '%', '*']
    #to_do finish this function. catch the exceptions.
    # @unittest.mock.patch('builtins.input', create= True)
    # def test_3(self, mock_input):
    #     mock_input.side_effect = 'xyXY'
    #     with self.assertRaises(Exception):
    #         result = ask_usrchoice()


if __name__ == "__main__":
    #here we can ask user if she wants to play mutiple times.
    #if yes, we can call os.system('game.py') in a while loop
    #Also, for repeating game, we can have os.system("cls")
    unittest.main()
