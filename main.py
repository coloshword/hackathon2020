import pygame
import pygame.gfxdraw
import levels
import button
import time

pygame.init()
pygame.display.set_caption('Type FAST')
menu_image = pygame.image.load('type2.png')
menu_image = pygame.transform.scale(menu_image, (400, 250))
# make the screen
running = True
char_objects = []
# Generate text
font = pygame.font.SysFont('Calibri', 25)


class Letters():
    def __init__(self, char, x, y, color=(255, 255, 255)):
        self.char = char
        self.x = x
        self.y = y
        self.color = color

    def char_display(self):
        txt = font.render(self.char, True, self.color)
        screen.blit(txt, (self.x, self.y))

    def become_green(self):
        self.color = (0, 255, 0)

    def become_red(self):
        self.color = (255, 0, 0)


def menu():
    global current_level
    current_level = 1
    screen = pygame.display.set_mode((900, 500))
    screen.fill((0, 191, 255))
    menu_run = True
    screen.blit(menu_image, (240, 20))
    title_font = pygame.font.SysFont('Calibri', 50)
    text = title_font.render('Touch Typer', True, (149, 85, 0))
    textRect = text.get_rect()
    screen.blit(text, textRect)
    about = button.draw_bordered_rounded_rect(screen, (180, 320, 150, 35), (177, 156, 217), (0, 0, 0), 5, 0, "About", (255, 255, 255), (225, 328))
    play = button.draw_bordered_rounded_rect(screen, (550, 320, 150, 35), (177, 156, 217), (0, 0, 0), 5, 0, "Play", (255, 255, 255), (600, 328))
    pygame.display.flip()
    while menu_run:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            elif play.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                menu_run = False
                run_level(levels.level1())
            elif about.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                menu_run = False
                about_menu()


def str_to_object(string):
    global char_objects
    char_objects = []
    x_cor = 50
    y_cor = 30
    skinny_letters ='j;fl'
    somewhat_skinny = 'r'
    somewhat_fat = 'SF'
    fat_letters = 'wAHDGK'
    obese_letters = 'm'
    index = 0
    for let in string:
        obj = Letters(let, x_cor, y_cor)
        char_objects.append(obj)
        if let in skinny_letters:
            x_cor += 5
        elif let in somewhat_skinny:
            x_cor += 7
        elif let in somewhat_fat:
            x_cor += 11
        elif let in fat_letters:
            x_cor += 13
        elif let in obese_letters:
            x_cor += 15
        else:
            x_cor += 10
        if index == 100:
            x_cor = 50
            y_cor += 60
            index = 0
        index += 1


def display_chars():
    global screen
    screen.fill((0, 0, 0))
    for char in char_objects:
        char.char_display()
    pygame.display.flip()


def about_menu():
    global above
    screen = pygame.display.set_mode((400, 600))
    screen.fill((250, 218, 221))
    back = button.draw_bordered_rounded_rect(screen, (130, 500, 150, 50), (177, 156, 217), (0, 0, 0), 5, 0, "Back", (255, 255, 255), (180, 515))
    about = True
    pygame.display.flip()
    while about:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if back.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                about = False
                pygame.display.flip()
                main()


def go_to_next():
    global current_level
    current_level += 1
    white_background = button.draw_bordered_rounded_rect(screen, (150, 200, 700, 200), (255, 255, 255), (0, 0, 0), 5, 0)
    next = button.draw_bordered_rounded_rect(screen, (430, 340, 150, 50), (177, 156, 217), (0, 0, 0), 10, 0, "Next", (255, 255, 255), (480, 355))
    pygame.display.flip()
    wait = True
    while wait:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if next.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if current_level == 2:
                    run_level(levels.level2())
                elif current_level == 3:
                    run_level(levels.level3())
                elif current_level == 4:
                    run_level(levels.level4())
                elif current_level == 5:
                    run_level(levels.level5())
                elif current_level == 6:
                    run_level(levels.level6())
                elif current_level == 7:
                    run_level(levels.level7())
                elif current_level == 8:
                    run_level(levels.level8())
                wait = False


def stay_on_level():
    white_background = button.draw_bordered_rounded_rect(screen, (150, 200, 700, 200), (255, 255, 255), (0, 0, 0), 5, 0)
    retry = button.draw_bordered_rounded_rect(screen, (430, 340, 150, 50), ((139, 0, 0)), (0, 0, 0), 10, 0, "Retry", (255, 255, 255), (480, 355))
    pygame.display.flip()
    wait = True
    while wait:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if retry.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if current_level == 1:
                    run_level(levels.level1())
                elif current_level == 2:
                    run_level(levels.level2())
                elif current_level == 3:
                    run_level(levels.level3())
                elif current_level == 4:
                    run_level(levels.level4())
                elif current_level == 5:
                    run_level(levels.level5())
                wait = False


def run_level(level):
    global running
    global screen
    str, total_time = level
    (width, height) = (1150, 600)
    screen = pygame.display.set_mode((width, height))
    screen.fill((0, 0, 0))
    str_to_object(str)
    display_chars()
    index = 0
    pygame.display.flip()
    ListOfLetters = [letter for letter in str]
    ListOfNums = []
    ListOfKeys = [0]
    start = 0
    for letter in ListOfLetters:
        number = ord(letter)
        ListOfNums.append(number)
    print(ListOfNums)
    while running:
        for event in pygame.event.get():
            if (index == len(str)):
                end = time.time()
                totalTime = levels.ElapsedTime(end, start)
                next = levels.checkAdvancement(totalTime, total_time)
                if next:
                    go_to_next()
                else:
                    stay_on_level()
                running = False
            if event.type == pygame.KEYDOWN:
                a = event.key
                if (start == 0 and index == 0):
                    start = time.time()
                if (a > 100000):
                    ListOfKeys.append(a)
                else:

                    if ListOfLetters[index].isupper():

                        if (ListOfKeys[-1] > 100000 and a == ListOfNums[index] + 32):
                            char_objects[index].become_green()
                            ListOfKeys.append(a)
                            index += 1
                        else:
                            char_objects[index].become_red()
                    elif a == ListOfNums[index]:
                        ListOfKeys.append(a)
                        char_objects[index].become_green()
                        index += 1
                    else:
                        char_objects[index].become_red()
                    display_chars()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


def main():
    global running
    global screen
    menu()


main()





