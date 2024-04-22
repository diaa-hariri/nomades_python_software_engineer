import random
import math

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """
    # Generate a random number between 1 and 100
    MAX_NUMBER = 10000
    MAX_COUNT = round(math.log2(MAX_NUMBER)) # math.log(MAX_NUMBER) / math.log(2)
    
    secret_number = random.randint(1, MAX_NUMBER)
    print(secret_number)
    number=int(input("Indiquez un nombre : "))
    count=1
    while(number!=secret_number):
        number = int(input("Indiquez un nombre : "))
        
        if number < secret_number:
            print("Le nombre est trop petit")
        elif number > secret_number:
            print("Le nombre est trop grand")

        count+=1

    assert number == secret_number

    # to ask user to enter the number use the function input
    if count < 7:
        print(f"bravo, tu as trouvé en moins de {MAX_COUNT} coups")
    elif count >= 7:
        print("Bravo vous avez trouvé, essayez de mieux faire la prochaine fois")

if __name__ == '__main__':
    # Run the game
    guess_number()
