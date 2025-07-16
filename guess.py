#importing the module random
import random as r

#setting the necessary variables to take inputs from the user
limit = int(input("Enter the limit: "))
random_number = r.randint(1, limit)
no_of_guesses = int(input("How many guesses do you want? "))

#initializing the guess variable
guess = 0

#the while block
while True:
    #if block
    if guess == no_of_guesses:
        print("You are out of guesses!")
        break
    user_guess = int(input("Enter your guess: "))
    guess += 1
    if user_guess == random_number:
        if guess == 1:
            print("You got the number right in a single guess, PERFECTO!")
            break
        else:
            print("You guessed the number right in", guess, "guesses!")
            break
    elif user_guess < random_number:
        print("You are below the number!")
    elif user_guess > random_number:
        print("You are above the number ")

        #Let us run the program

        #THANKYOU!