import random

print('*****Random Number Guess Menu*****')
print('You have 3 guesses to answer correctly')
print('The number lies between 1 and 10')
print('')
print('')
print('Good Luck!') 
print('')
"""
Code above is the menu that prints before the game
Code below is the game and it's properties
"""
guessCount = 0 # iterateable number that will add 1 each guess
guessLimit = 3 # Once guess count reaches 3 the program ends
answer = random.randint(1, 10) # This is the random number which is the answer to the random guess, random every game
while guessCount < guessLimit:  # iterate the turns until user runs out (while 0 < 3) 
    guess = int(input('Guess: ')) # user guess
    guessCount += 1 # keep user out of infinite loop
    if guess == answer: # if guess is correct
        print("You guessed it!")
        guessCount += 3 # ends game by adding 3 to the turns
    else: # if guess is incorrect
        print('Incorrect guess')
     
