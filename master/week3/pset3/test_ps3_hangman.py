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

    print(purple("-----------------------------------------------------------"))
    print(purple("test_is_word_guessed"))
    print(purple("-----------------------------------------------------------"))

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
    print(purple("-----------------------------------------------------------"))
    print(purple("test_is_word_guessed"))
    print(purple("-----------------------------------------------------------"))

    function_call = "getGuessedWord(\"apple\", ['e', 'i', 'k', 'p', 'r', 's'])"
    expected_result = "_ pp_ e"
    received_result = getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    function_call = "getGuessedWord(\"apple\", ['a', 'p', 'l', 'e'])"
    expected_result = "apple"
    received_result = getGuessedWord("apple", ['a', 'p', 'l', 'e'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    function_call = "getGuessedWord(\"apple\", ['b', 'a', 'n'])"
    expected_result = "a_ _ _ _ "
    received_result = getGuessedWord("apple", ['b', 'a', 'n'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

def test_get_available_letters():
    print(purple("-----------------------------------------------------------"))
    print(purple("test_get_available_letters"))
    print(purple("-----------------------------------------------------------"))

    function_call = ("getAvailableLetters(['a'])")
    expected_result = "bcdefghijklmnopqrstuvwxyz"
    received_result = getAvailableLetters(['a'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    function_call = ("getAvailableLetters(['a', 'b', 'd'])")
    expected_result = "cefghijklmnopqrstuvwxyz"
    received_result = getAvailableLetters(['a', 'b', 'd'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    function_call = "getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])"
    expected_result = "abcdfghjlmnoqtuvwxyz"
    received_result = getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

if __name__ == "__main__":
    test_is_word_guessed()
    test_get_guessed_word()
    test_get_available_letters()
