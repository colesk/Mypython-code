from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print  random_number
guesses_left = 3
# Start your game!
while guesses_left>=0:
    ip = int(raw_input("Guess the number"))
    print ip 
    
    if ip == random_number :
        print("correct guess")
        break
    guesses_left = guesses_left - 1
