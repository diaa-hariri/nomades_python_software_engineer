def sum(tableau: list[int]) -> int: # O(n)
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    """
    somme = 0
    for nombre in tableau:
        somme = somme + nombre
    return somme


def average(tableau: list[int]) -> float: # O(n)
    """
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    # somme = 0
    # for nombre in tableau:
    #     somme = somme + nombre
    # return somme / len(tableau)
    return sum(tableau) / len(tableau)


def min(tableau: list[int]) -> int:
    """
    Function that returns the minimum of the elements of the array
    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    min_ = tableau[0]
    for i in range(1, len(tableau)):
        if tableau[i] < min_:
            min_ = tableau[i]
    return min_


def max(tableau: list[int]) -> int:
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """
    max_ = tableau[0]
    for i in range(1, len(tableau)):
        if tableau[i] > max_:
            max_ = tableau[i]
    return max_


def min_max(tableau: list[int]) -> tuple[int, int]:
    """
    Function that returns the minimum and maximum of the elements of the array
    :param tableau: the array to find the minimum and maximum of
    :return: the minimum and maximum of the elements of the array
    """
    # min_ = min(tableau)
    # max_ = max(tableau)

    min_ = tableau[0]
    max_ = tableau[0]
    for i in range(1, len(tableau)):
        if tableau[i] > max_:
            max_ = tableau[i]
        if tableau[i] < min_:
            min_ = tableau[i]

    return (min_, max_)


def mode(tableau: list[int]) -> int:
    """
    Function that returns the mode of the elements of the array
    The mode is the value that appears most often in a set of data values.
    If there is a tie, the mode is the smallest value.
    :param tableau: the array to find the mode of
    :return: the mode of the elements o  f the array
    """
    # mode_num = tableau[0]

    # for i in range(1, len(tableau)):
    #     if mode_num == tableau[1]:
    #         mode_num = tableau[1]
    #     elif mode_num == tableau[1]+1:
    #         mode_num = tableau[1]
    #     elif mode_num > tableau[i]:
    #         mode_num = tableau[i]
    # return mode_num

    occurences = {}
    for num in tableau:
        if num not in occurences:
            occurences[num] = 0

        occurences[num] += 1
    
    obs_max = max(list(occurences.values()))
    ties = []

    for i, j in occurences.items():
        if j == obs_max:
            ties.append(i)
    
    return min(ties)


def variance(tableau: list[int]) -> float:
    """
    Function that returns the variance of the elements of the array
    :param tableau: the array to find the variance of
    :return: the variance of the elements of the array
    """
    mean = average(tableau)   #O(n)
    # var = sum([(x-mean)**2 for x in tableau])/len(tableau)
    var = 0
    for x in tableau:       # O(n)
        var += (x-mean)**2 
    return var / len(tableau)

def standard_deviation(tableau: list[int]) -> float:
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    :param tableau: the array to find the standard deviation of
    :return: the standard deviation of the elements of the array
    """
    return variance(tableau)**(1/2)

    import math
    return math.sqrt(variance(tableau))


def exist(tableau: list[int], valeur: int) -> bool:
    """
    Function that returns True if the value exists in the array
    :param tableau: the array to check if the value exists in
    :param valeur: the value to check if it exists in the array
    :return: True if the value exists in the array, False otherwise
    """
    # return valeur in tableau 
    # if valeur in tableau:
    #     return True

    # return False

    for x in tableau:
        if x == valeur:
            return True
    return False


def position(tableau: list[int], valeur: int) -> int:
    """
    Function that returns the position of the first value in the array
    If the value does not exist in the array, it returns -1
    :param tableau: the array to find the position of
    :param valeur: the value to find the position of
    :return: the position of the value in the array
    """
    for i, v in enumerate(tableau):
        if v == valeur:
            return i
    return -1


def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    # return arr1 == arr2

    if len(arr1) != len(arr2):
        return False
    
    assert len(arr1) == len(arr2)
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True
        


def is_list(tableau) -> bool:
    """
    Function that returns True if the array is a table
    :param tableau: the array to check if it is a table
    :return: True if the array is a table, False otherwise
    """
    return type(tableau) == 'list'


def is_list_of_numbers(tableau) -> bool:
    """
    Function that returns True if the array is a table of numbers
    :param tableau: the array to check if it is a table of numbers
    :return: True if the array is a table of numbers, False otherwise
    """
    if len(tableau) == 0:
        return False
    
    for number in tableau:
        if type(number) != 'int':
            return False
    return True

def sort_ascending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in ascending order 
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    # n = len(arr)

    # for i in range(n):
    #     for x in range(n-i-1):
    #         if arr[x] > arr[x+1]:
    #             arr[x], arr[x+1] = arr[x+1], arr[x]
    # return arr 
    # import math

    # out = []

    # for _ in range(len(arr)):
    #     out.append(arr[arr.index(min(arr))])
    #     arr[arr.index(min(arr))] = math.inf
    
    # return out

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
          if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
    return arr
            



def sort_descending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
          if arr[j] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
    return arr

def median(tableau: list[int]) -> int:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """
    arr = sort_ascending(tableau)
    mid = len(arr)//2
    return arr[mid] if len(arr)%2==1 else (arr[mid-1] + arr[mid]) / 2
