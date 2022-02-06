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


def is_palindrome_number(n):
    reverse = reverse_number(n)
    return reverse == n


def reverse_number(n):
    digits = number_of_digits(n)
    result = 0
    while n > 0:
        last_digit = n % 10
        result += last_digit * (10 ** (digits - 1))
        digits -= 1
        n = n // 10
    
    return result

def reverse_number_better(n):
    reverse = 0
    while n > 0:
        last_digit = n % 10
        reverse = reverse * 10 + last_digit
        n = n // 10
    return reverse


def factorial(n):
    if n < 0:
        raise ValueError("Bro, give correct value")
    if n < 2:
        return n
    else:
        return n * factorial(n - 1)
    

"""This is what I had in memory, it is REALLY WRONG"""
# def gcd(a, b):
#     while a % b != 0:
#         b = a % b
#     return b

"""Here is the correct implementation"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

"""My own implementation of LCM, which is of course the Naive implementation of the LCM """
def lcm_naive(a, b):
    if a < b:
        return lcm(b, a) 
    if a % b == 0:
        return a
    counter = 1
    val = b

    while val % a != 0:
        val = b * counter
        counter += 1

    return val

"""The proper implementation uses the GCD!! 
So the formula is -> GCD(a,b) * LCM(a,b) = a * b
Also, note that GCD is same as HCF"""
def lcm(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    return a * b // gcd(a, b)
