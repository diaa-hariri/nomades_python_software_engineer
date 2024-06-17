def is_even(number: int) -> str:
    """
    Function that checks if a number is even or odd.
    Return the string "The number is even" if the number is even, "The number is odd" otherwise.
    params:
      number: The number to check
    
    Returns:
      A string that says if the number is even or odd
    """
    # if number % 2 == 0:
    #     return "The number is even"

    # return "The number is odd" 

    return "The number is even" if number % 2 == 0 else "The number is odd" 

        

def factorial(n: int) -> int:
    """
    Function that computes the factorial of a number.
    The factorial of n is the product of all positive integers less than or equal to n.
    :param n: The number to compute the factorial of
    :return: The factorial of n
    # """
    # if n < 0:
    #     raise ValueError("Number should be positive")
    # elif n == 0:
    #     value = 1
    # else:
    #     result = 1 
    #     for i in range(2, n+1):
    #         result *= i
    #     value = result
    # return value

    if n == 0:
        return 1
    
    return n * factorial(n-1)

# factorial(5)
# return 5 * factorial(4)
# 5 * (4 * factorial(3))
# 5 * (4 * (3 *factorial(2)))
# 5 * (4 * (3 * (2* factorial(1))))
# 5 * (4 * (3 * (2* (1 * factorial(0)))))
# 120

def fibonacci(n: int) -> int:
    """
    Function that computes the nth Fibonacci number.
    :param n: The index of the Fibonacci number to compute
    :return: The nth Fibonacci number
    """
    if n < 2:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)


def sum(n: int) -> int:
    """
    Function that computes the sum of all integers from 0 to n.
    :param n: The number to compute the sum up to
    :return: The sum of all integers from 0 to n
    """
    return n*(n+1)/2 # O(1)

    sum = 0 # O(n)
    for i in range(0, n+1):
        sum += i
    return sum

def square(n: int) -> int:
    """
    Function that computes the square of a number.
    :param n: The number to compute the square of
    :return: The square of n
    """
    return n*n



def is_prime(n: int) -> bool:
    """
    Function that checks if a number is prime.
    A prime number is a number that is divisible only by itself and 1.
    :param n: The number to check
    :return: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    
    for i in range(2, n**(1/2)):
        if n%i==0:
            return False
    return True