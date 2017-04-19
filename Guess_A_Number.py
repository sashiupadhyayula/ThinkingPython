import random

def checkForCorrectNumber(guessNum):
    if guessNum > randomNum:
        return 'number too large'
    elif guessNum < randomNum:
        return 'number too small'
    else:
        return 'Bingo!'

print("Guess a number between 1 and 20")
randomNum = random.randint(1,20)
for guessesTaken in range(1,7):
    guessNum = int(input())
    _correctGuess = checkForCorrectNumber(guessNum)
    print(_correctGuess)
    if _correctGuess == 'Bingo!':
        print('You guessed right. Don\'t continue the loop')
        break
    else:
        print('Number of guesses taken: ' + str(guessesTaken))
        print('Continuing the loop')
        continue

    # guessesTaken = guessesTaken + 1


if guessesTaken <= 7:
    print('You guessed in ' + str(guessesTaken) + ' guesses')
else:
    print('You ran out of guesses')

