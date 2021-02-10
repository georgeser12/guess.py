import random


secretNumber = random.randint(1, 10)


def play_again():
    print('play again (yes or no): ')
    return input('').lower().startswith('y')

def get_guess():
    global secretNumber
    winner = True
    guesses = 5
    print("range: (1-10)")
    numbers = []
    while winner:
        try:
            guess = int(input('Guess a number: '))


            if guess == secretNumber:
                print(f'YES! the secret number was {secretNumber}')
                winner = False

            elif guess in numbers:
                print("you already guessed this number")

            elif guess not in range(1,10):
                print('that number was not within the range')

            elif guess != secretNumber:
                guesses -= 1
                print('Nope incorrect')
                numbers.append(guess)


            if guesses == 0:
                print(f'sorry you ran out of tries, the answer was {secretNumber}')
                winner = False
        except ValueError:
            print('invalid response')

    if winner == False:
        if play_again():
            winner = True
            secretNumber = random.randint(1, 10)
            get_guess()
        else:
            quit()


get_guess()

