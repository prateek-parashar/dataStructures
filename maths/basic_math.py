import math
from unittest import result

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

"""Algorithm to check if a number is prime 
This method is thanks to the time I spent on codeWars!!
This idea is based on the fact that each divisor of a number appear in pairs. 
And in that pair, one number is less than square root of n, and the other is greater than 
the square root of n

One thing to keep in note is, you don't need to use the squareroot function, in the for loop
I can iterate while i * i < n"""

def is_prime(n):
    if n == 2:
        return True

    if n == 1 or n % 2 == 0:
        return False
    
    import math
    root_of_n = math.floor(math.sqrt(n))
    for i in range(2, root_of_n + 1):
        if n % i == 0:
            return False
    
    return True

"""This was the implementatation I came up with but fml, I don't need to check if the number is prime or not!"""
def prime_factors(n):
    result = []
    for i in range(n):
        if i * i > n:
            break

        if is_prime(i):
            check = n
            while check % i == 0:
                result.append(i)
                check = check // i
    return result

def prime_factors_better(n):
    result = []
    if n <= 1:
        return

    for i in range(2, n):
        if i * i > n:
            break
        
        while n % i == 0:
            result.append(i)
            n = n // i
        
    if n > 1:
        result.append(n)
    return result


def all_factors(n):
    result = []
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            result.append(i)
            if n // i != i:
                result.append(n // i)
    return result

"""Sieve of Erathosthenes"""
"""This algorithm returns all the prime numbers less than the given number"""
"""A naive approach would be to iterate over all the values less than n
check if that number is prime
And then add the number """

def return_primes(n):
    result = []
    master_table = [1 for i in range(n)]

    # Mark the first 2 values corresponding to 0 and 1 as false
    master_table[0] = 0
    master_table[1] = 0

    # Mark all multiples of 2 as false
    for i in range(4, n, 2):
        master_table[i] = 0

    # Mark all multiples of 3 as false
    for i in range(6, n, 3):
        master_table[i] = 0

    # Mark all multiples of 2 as false
    for i in range(10, n, 5):
        master_table[i] = 0

    for i in range(n):
        if master_table[i] == 1:
            result.append(i)
        
    return result