import random

guess=(random.randint(1,50))

while True:
    
    n=int(input("Enter Number:"))
    
    if n==guess:
        print("You guessed currect Number.")
        break;
    elif n<guess:
        print("You guessed Smaller Number.")
    elif n>guess:
        print("You guessed Bigger Number.")



    
