import random
import string

def generator():
    result = []
    for i in range(1,9):
        r = random.randint(1, 2)
        if r == 1:
            result.append(random.choice(string.ascii_letters))
        elif r == 2:
            result.append(random.randint(0, 9))

    print("https://pastebin.com/",*result, sep = '')

print('#########################')
print('')
print('Welcome to the Pastebin Generator !')
print('')
print('#########################')
print('')

linksWanted = int(input('How many links do you want ?       '))

def makeRandom():
    finishedLinks = 0
    while (finishedLinks < linksWanted):
        randomShit = generator()
        finishedLinks = finishedLinks + 1

makeRandom()