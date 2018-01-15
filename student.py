"""

Write code that, given `my_str`, returns True if that string is a palindrome,
and False otherwise.

A palindrome is a word/phrase that is the same backwards as forwards (e.g. "race car").
Single-letter strings (e.g. "I") should be considered palindromes

You may assume that the input is a valid, lower-case string. However, the string
might have white-space, which you should remove.

HINT: If the first and last letters don't match, you know for a fact that the string
can't be a palindrome. Use your control flow tools to make your code more efficient
by stopping execution as soon as you know the answer.

"""


def my_function(my_str):
    """ Parameters
        ----------
        my_str : str
            The word/phrase to be analyzed

        Returns
        -------
        True if my_str is a palindrome, False otherwise.
    """

    my_str = my_str.replace(" ", "")
    while len(my_str) > 1:
        if my_str[0] == my_str[len(my_str) - 1]:
            my_str = my_str[1:len(my_str) - 1]
        else:
            return False

    return True
