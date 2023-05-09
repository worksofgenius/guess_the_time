import random

secret_time = random.randint(1, 20)

print('I spent between 1 and 20 minutes on this code.')

# Ask the player to guess 6 times

for guesses_taken in range(1, 7):
    print('Guess how long!')
    guess = int(input())

    if guess < secret_time:
        print('I wish! Your guess is too low.')
    elif guess > secret_time:
        print('I\'m not that dumb. Your guess is too high.')
    else:
        break

if guess == secret_time:
    print('How did you know?! You guessed it in ' + str(guesses_taken) + ' tries!')
else:
    print('Wow! You couldn\'t even guess in ' + str(guesses_taken) + ' tries. It took ' + str(secret_time) + ' minutes.')