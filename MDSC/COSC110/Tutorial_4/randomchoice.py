import random
choice = random.randint(1,20)
correct = False
print('I\'m thinking of a number between 1 and 20... try and guess what it is!: ')
while correct == False:
    guess = int(input())
    if guess < choice:
        print('Nope, sorry! Higher... try again: ')
    elif guess > choice:
        print('Nope, sorry! Lower... try again: ')
    else:
        correct = True
        print(f'Ding ding ding! That\'s right, I was thinking of {choice}!')
    