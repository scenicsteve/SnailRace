"""Snail Race, by Al Sweigart al@inventwithpython.com
Fast-paced snail racing action!
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, beginner, game, multiplayer"""

import random, time, sys

# Set Up Constrants:max_name_length
max_num_snails = 8
max_name_length = 20
Finish_line = 40

print('''Snail Race, by Al Sweigart w/ Edits from ScenicSteve
    @v <-- snail

''')

#Ask how many snails to race:
while True: # keep asking until player enters number
    print('How many snails will race? Max:', max_num_snails)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= max_num_snails:
            break
    print('Enter a number between 2 and', max_num_snails)

# Enter the names of each snail:
snailNames = [] # lsit of the string snail names
for i in range(1, numSnailsRacing + 1):
    while True: # Keep asking until player enters a valid name.
        print('Enter snail #' + str(i) + "'s name:")
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not already been used.')
        else:
            break # name entered is accepted
    snailNames.append(name)

# Display each snail at the start line.
print('\n' * 40)
print('START' + (' ' * (Finish_line - len('START')) + 'FINISH'))
print('|' + (' '* (Finish_line - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:max_name_length])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5) # pause at start of race

while True: #main program loop.
    #pick random snails to move forward:
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

    #check if a snail has reached the finish
        if snailProgress[randomSnailName] == Finish_line:
            print(randomSnailName, 'has won!')
            sys.exit()

    time.sleep(0.5)

    print('\n' * 40)

    #Display start and finish lines
    print('START' + (' ' * (Finish_line - len('START')) + 'FINISH'))
    print('|' + (' ' * (Finish_line - 1) + '|'))

    #Display the snails (with name tags):
    for snailName in snailNames:
        space = snailProgress[snailName]
        print((' ' * space) + snailName[:max_name_length])
        print(('.' * snailProgress[snailName]) + '@v')