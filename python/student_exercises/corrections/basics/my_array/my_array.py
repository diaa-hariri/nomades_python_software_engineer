from functools import reduce
def sum(tableau: list[int]) -> int:
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    [1,2,3,4,5]
    """
    # total = 0
    # for value in tableau:
    #     total += value
    # return total

    # total = 0
    # for i in range(len(tableau)):
    #     total += tableau[i]
    # return total
  
    return reduce(lambda pv, cv: pv+cv, tableau, 0)

def average(tableau: list[int]) -> float:
    """
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    return sum(tableau) / len(tableau)



def min(tableau: list[int]) -> int:
    """
    Function that returns the minimum of the elements of the array
    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    # mini = tableau[0]
    # for element in (tableau[1:]):
    #     if element < mini:
    #         mini = element
    # return mini

    # [10, 100, 2, 7, 19, 1]

    mini = tableau[0]
    for i in range(1, len(tableau), 1):
        if tableau[i] < mini:
            mini = tableau[i]
    return mini

def max(tableau: list[int]) -> int:
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """
    maxi = tableau[0]
    for i in range(1, len(tableau), 1):
        if tableau[i] > maxi:
            maxi = tableau[i]
    return maxi


def min_max(tableau: list[int]) -> tuple[int, int]:
    """
    Function that returns the minimum and maximum of the elements of the array
    :param tableau: the array to find the minimum and maximum of
    :return: the minimum and maximum of the elements of the array
    """
    return (min(tableau), max(tableau))

    # maxi = mini = tableau[0]
    # for i in range(1, len(tableau), 1):
    #     curr_elem = tableau[i]
    #     if curr_elem < mini:
    #         mini = curr_elem
    #     if curr_elem > maxi:
    #         maxi = curr_elem
    
    # return mini, maxi

    # minimum = maximum = tableau[0]

    # for i in tableau:
    #     if i < minimum:
    #         minimum = i
    #     if i > maximum:
    #         maximum = i

    # return minimum, maximum



def mode(tableau: list[int]) -> int:
    """
    Function that returns the mode of the elements of the array
    The mode is the value that appears most often in a set of data values.
    If there is a tie, the mode is the smallest value.
    :param tableau: the array to find the mode of
    :return: the mode of the elements of the array
    """
    return None

def variance(tableau: list[int]) -> float:
    """
    Function that returns the variance of the elements of the array
    :param tableau: the array to find the variance of
    :return: the variance of the elements of the array
    [1,2,3,4,5]
    """
    # mean = average(tableau)           O(n)

    # variance = 0                      O(1)
    # for xi in tableau:                O(n)
    #     variance += (xi - mean)** 2   (O(1)*n) -> O(n)
    
    # return variance / len(tableau)    O(1) 

    variance = 0                              #O(1) // O(n^2)
    for xi in tableau:                        #O(n)
        variance += (xi-average(tableau))**2  #(O(n)*n) -> O(n^2)
    
    return variance / len(tableau)            #0(1)

def standard_deviation(tableau: list[int]) -> float:
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    :param tableau: the array to find the standard deviation of
    :return: the standard deviation of the elements of the array
    """
    return None


def exist(tableau: list[int], valeur: int) -> bool:
    """
    Function that returns True if the value exists in the array
    :param tableau: the array to check if the value exists in
    :param valeur: the value to check if it exists in the array
    :return: True if the value exists in the array, False otherwise
    """
    return None


def position(tableau: list[int], valeur: int) -> int:
    """
    Function that returns the position of the first value in the array
    If the value does not exist in the array, it returns -1
    :param tableau: the array to find the position of
    :param valeur: the value to find the position of
    :return: the position of the value in the array
    """
    return None


def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    return None


def is_list(tableau) -> bool:
    """
    Function that returns True if the array is a table
    :param tableau: the array to check if it is a table
    :return: True if the array is a table, False otherwise
    """
    # return type(tableau) == list 

    # if(type(tableau) == list):
    #     return True
    # else: 
    #     return False
    
    return True if type(tableau) == list else False


def is_list_of_numbers(tableau) -> bool:
    """
    Function that returns True if the array is a table of numbers
    :param tableau: the array to check if it is a table of numbers
    :return: True if the array is a table of numbers, False otherwise
    """
    if not is_list(tableau) or tableau == []:
        return False
    
    for elem in tableau:
        if(type(elem) != int or type(elem) != float or type(elem) != complex):
            return False
    
    return True
        


def sort_ascending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in ascending order 
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    return None


def sort_descending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    return None

def median(tableau: list[int]) -> int:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """
    return None