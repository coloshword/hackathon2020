import random


def randomSpaces():
    numberOfspaces = random.randint(1, 12)
    return numberOfspaces
randomSpaces()



def level1():
    possibleLetters = ['a','s','d','f','g','h','j','k',";"];
    string2solve = ""
    i = 0;
    spaces = randomSpaces()
    while i < 500:
        if (spaces == 0):
            string2solve = string2solve + " "
            spaces = randomSpaces()
        else:
            spaces = spaces - 1
        a = random.choice(possibleLetters)
        string2solve = string2solve + a
        i = i + 1
    return string2solve
level1()

def level2():
    possibleLetters = ['a','s','d','f','g','h','j','k', "r","e","u","i"]
    string2solve = ""
    i = 0;
    spaces = randomSpaces()
    while i < 500:
        if (spaces == 0):
            string2solve = string2solve + " "
            spaces = randomSpaces()
        else:
            spaces = spaces - 1
        a = random.choice(possibleLetters)
        string2solve = string2solve + a
        i = i + 1
    return string2solve
level2()