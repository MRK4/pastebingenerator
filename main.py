import random
import string
from colorama import Fore

def generator():
    result = []
    for i in range(1,9):
        r = random.randint(1, 2)
        if r == 1:
            result.append(random.choice(string.ascii_letters))
        elif r == 2:
            result.append(random.randint(0, 9))
    print("https://pastebin.com/",*result, sep = '')

print(Fore.YELLOW)
print('')
print('    ____             __       __    _       ______                           __            ')
print('   / __ \____ ______/ /____  / /_  (_)___  / ____/__  ____  ___  _________ _/ /_____  _____')
print('  / /_/ / __ `/ ___/ __/ _ \/ __ \/ / __ \/ / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/')
print(' / ____/ /_/ (__  ) /_/  __/ /_/ / / / / / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    ')
print('/_/    \__,_/____/\__/\___/_.___/_/_/ /_/\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     ')
print('')
print('                                                                                     by MRK')
print('')
print(Fore.RESET)
print('Welcome to the PastebinGenerator !')
print('')
print(Fore.RED)
print('please remember that a lot of the links are dead, use a checker or test them yourself.')
print(Fore.RESET)

linksWanted = int(input('How many links do you want ?       '))

def makeRandom():
    finishedLinks = 0
    while (finishedLinks < linksWanted):
        randomShit = generator()
        finishedLinks = finishedLinks + 1
        
print('')
makeRandom()

print(Fore.LIGHTGREEN_EX)
print('')
print("Done!")
print(Fore.RESET)