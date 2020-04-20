import random


# Game menu
print("Welcome to Random Guess! \n")
print("Please Select your mode.")
print('Hard   - Guess between 0 and 1000')
print('Medium - Guess between 0 and 100')
print('Easy   - Guess between 0 and 10')


# Select the difficulty level
while True:
    mode=input('H-Hard, M-Medium, E-Easy(default): ')

    if (mode.lower()=='h'):
        rng=1000
        break
    elif (mode.lower()=='m'):
        rng=100
        break
    elif (mode.lower()=='e'):
        rng=10
        break 
    else:
        print('Error! Please enter valid mode.')


# Generate random number
rand_num=random.randrange(rng)


# Count user attempts
user_count=0


# Loop through until user the guess' the number
while True:
    user_count+=1  #count user attempts
   
    # Take user input(guessed number)
    guess=input("Can you guess the number? ")
    guess=int(guess)


    if guess == rand_num:
        print("You are correct!")
        break
    elif guess>rand_num:
        print("Wrong! You were too high.")
    elif guess<rand_num:
        print('Wrong! You were too low.')
































