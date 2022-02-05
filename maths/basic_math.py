import math

def number_of_digits(n):
    """This is the first solution I came up with, but then it uses the 
    convinience of it being python

    return len(str(n))
    
    """

    """The mathematical way of doing this would be to 
    maintain a count variable where we update it after every 
    time the number > 0 after every time we divide it by 10 """

    """Woaaah, the best way is to do it by log!
    the log of a number to base 10 + 1 floored would give the number of digits"""

    return math.floor(math.log(n, 10) + 1) 