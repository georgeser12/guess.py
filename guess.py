import random


#picking random number
secretNumber = random.randint(1, 10)


#play again feature
def play_again():
    print('play again (yes or no): ')
    return input('').lower().startswith('y')


#getting player guess
def get_guess():
    global secretNumber
    
    #variables
    winner = True
    guesses = 5
    print("range: (1-10)")
    numbers = []
    #loop to get guesses
    while winner:
        try:
            guess = int(input('Guess a number: '))

            #make sure if they got the right number
            if guess == secretNumber:
                print(f'YES! the secret number was {secretNumber}')
                winner = False
                
            #checking if they already guessed that number
            elif guess in numbers:
                print("you already guessed this number")

             #making sure the guess is within range
            elif guess not in range(1,10):
                print('that number was not within the range')

            # if they get the number wrong, you lose tries
            elif guess != secretNumber:
                guesses -= 1
                print('Nope incorrect')
                numbers.append(guess)

            #run out of guesses, game ends
            if guesses == 0:
                print(f'sorry you ran out of tries, the answer was {secretNumber}')
                winner = False
        # expecting Valueerrors and returning a 'invalid response' instead of crashing
        except ValueError:
            print('invalid response')
    # if game ends ask if they'd like to play again
    if winner == False:
        if play_again():
            winner = True
            secretNumber = random.randint(1, 10)
            get_guess()
        else:
            quit()


get_guess()

