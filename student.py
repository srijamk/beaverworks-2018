""" Write code that, given x (an integer), returns the string "three" if x is a multiple of 3, "five" if x is a
    multiple of 5 and the string "threefive" if x is a multiple of both 3 and 5.

    If none of those conditions are true, simply return x.

    You may assume that your input is an integer >= 1
"""

def my_function(x):
    """ Parameters
        ----------
        x : int
            An integer > 0.

        Returns
        -------
        Union[str, int]
            Either "three", "threefive", or x.
    """
    # REMOVE "pass" AND WRITE YOUR CODE HERE
    if x % 3 == 0 and x % 5 != 0:
        return "three"
    elif x % 5 == 0 and x % 3 != 0:
        return "five"
    elif x % 3 == 0 and x % 5 == 0:
        return "threefive"
    return x