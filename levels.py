import random

def randomSpaces():
    numberOfspaces = random.randint(1, 12)
    return numberOfspaces
randomSpaces()

def ElapsedTime(end, start):
    totalTime = end - start
    return totalTime


def limits(index):
    index = index - 1;
    limits = [10,10,10,10,10]
    return limits[index]


def checkAdvancement(elapsedTime, limit):
    if (elapsedTime <= limit):
        print("Congrats, you passed!!")
        return True
    else:
        print("You suck lol")
        return False

def mainProcess(list):
    i = 0
    spaces = randomSpaces()
    string2solve = ""
    while i < 10:
        if (spaces == 0):
            string2solve = string2solve + " "
            spaces = randomSpaces()
            a = random.choice(list)
            string2solve = string2solve + a
            spaces = spaces - 1
        else:
            spaces = spaces - 1
            a = random.choice(list)
            string2solve = string2solve + a
        i = i + 1
    return string2solve

def level1():
    possibleLetters = ['a','s','d','f','g','h','j','k',";"];
    string2solve = mainProcess(possibleLetters)
    time = 10
    return string2solve, time


def level2():
    possibleLetters = ['a','s','d','f','g','h','j','k', "r","e","u","i"]
    string2solve = mainProcess(possibleLetters)
    time = 9
    return string2solve, time


def level3():
    possibleLetters = ['a','s','d','f','g','h','j','k', "r","e","u","i"
                       'q', 'w', 'o', 'p']
    time = 8
    string2solve = mainProcess(possibleLetters)
    return string2solve, time

def level4():
    possibleLetters = ['a','s','d','f','g','h','j','k', "r","e","u","i"
                       'q', 'w', 'o', 'p', 'c', 'v', 'b', 'n']
    string2solve = mainProcess(possibleLetters)
    time = 7
    return string2solve, time

def level5():
    possibleLetters = ['a','s','d','f','g','h','j','k',"r","e","u","i"
                       'q', 'w', 'o', 'p', 'c', 'v', 'b', 'n', 'z', 'x','m']
    string2solve = mainProcess(possibleLetters)
    time = 6
    return string2solve, time
