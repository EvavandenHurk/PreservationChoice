import random
import time

def displayIntro():
    print('''You are at your desk behind your computer. You have a new digital
archive that you want to preserve. You have three options: conversion, migration
or emulation''')
    print()

def choosePres():
    preservation = ''
    while preservation != '1' and preservation != '2' and preservation !='3':
        print('Which option will you choose? (1, 2 or 3)')
        preservation = input()

    return preservation

def checkPres(chosenPres):
    print('You set the preservation workflow into motion')
    time.sleep(2)
    print('It takes forever...')
    time.sleep(2)
    print('A new screen opens on your computer and...')
    print()
    time.sleep(2)

    conversionPres = random.randint(1, 3)
    migrationPres = random.randint(1, 3)

    if chosenPres == str(conversionPres):
        print('The screen freezes... All files are lost!')
    elif chosenPres == str(migrationPres):
        print('Lo and behold: the archive has been saved!')
    else:
        print('Hmm not the result you were looking for. Maybe another strategy?')

playAgain = 'yes'
while playAgain == 'yes' or playAgain =='y':
    displayIntro()
    presNumber = choosePres()
    checkPres(presNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
