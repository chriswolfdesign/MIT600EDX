#
# test_ps3_hangman.py
#
# A script that will allow me to create test cases for pset3's ps3_hangman.py
#
# Chris Wolf
# chriswolfdesign@gmail.com
#

from success_or_fail import *
from ps3_hangman import *

def test_is_word_guessed():

    function_call = "isWordGuessed(\"apple\", ['a', 'p', 'p', 'l', 'e'])"
    expected_result = True
    received_result = isWordGuessed("apple", ['a', 'p', 'p', 'l', 'e'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    function_call = "isWordGuessed(\"apple\", ['e', 'l', 'p', 'p', 'a'])"
    expected_result = True
    received_result = isWordGuessed("apple", ['e', 'l', 'p', 'p', 'a'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    function_call = "isWordGuessed(\"apple\", ['e', 'i', 'k', 'p', 'r', 's'])"
    expected_result = False
    received_result = isWordGuessed("apple", ['e', 'i', 'k', 'p', 'r', 's'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

def test_get_guessed_word():
    function_call = "getGuessedWord(\"apple\", ['e', 'i', 'k', 'p', 'r', 's'])"
    expected_result = "_ pp_ e"
    received_result = getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

if __name__ == "__main__":
    test_is_word_guessed()
    test_get_guessed_word()
