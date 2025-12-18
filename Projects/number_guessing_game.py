import random
# Number Guessing Game 
print("Welcome to 'Guess the number' game.")

run = True
# A loop to run game, Until the correct guess.
while(run):
    # random number generator between 1 to 100.
    rand_no = random.randint(2,99)
    # A counter variable which use to store number of guesses.
    count = 0
    while(True):
        user_guess = int(input("Guess the number: "))
        count = count + 1
        if rand_no == user_guess:
            print("Hooray! You guess the correct number.")
            break
        elif rand_no > user_guess:
            print("Too low!, Guess high\n")
        elif rand_no < user_guess:
            print("Too high!, Guess low\n")
    
    print("You Guess the number in ",count," attempts.\n")
    # Add a conditon if you want play or not 
    play = input("Do you want to play again? (y/n)")
    if 'n' == play.lower():
        run = False