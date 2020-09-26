import pygame
import pygame.gfxdraw
import levels
import button

pygame.init()
pygame.display.set_caption('Type FAST')
menu_image = pygame.image.load('type2.png')
menu_image = pygame.transform.scale(menu_image, (400, 250))
# make the screen
running = True
char_objects = []
# Generate text
font = pygame.font.SysFont('Calibri', 25)
str = levels.level1()
ListOfLetters = [letter for letter in str]
ListOfNums = []
for letter in ListOfLetters:
    number = ord(letter)
    ListOfNums.append(number)


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
    screen = pygame.display.set_mode((900, 500))
    screen.fill((0, 191, 255))
    menu_run = True
    pygame.display.flip()
    screen.blit(menu_image, (240, 20))
    choose_levels = button.draw_bordered_rounded_rect(screen, (180, 320, 150, 35), (177, 156, 217), (0, 0, 0), 5, 0, "Choose Levels", (255, 255, 255), (183, 328))
    play = button.draw_bordered_rounded_rect(screen, (550, 320, 150, 35), (177, 156, 217), (0, 0, 0), 5, 0, "Play", (255, 255, 255), (600, 328))
    pygame.display.flip()
    while menu_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_run = False
                pygame.quit()


def str_to_object(string):
    global char_objects
    x_cor = 50
    y_cor = 30
    skinny_letters ='j;fl'
    index = 0
    for let in string:
        obj = Letters(let, x_cor, y_cor)
        char_objects.append(obj)
        if let in skinny_letters:
            x_cor += 5
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


def main():
    global running
    global screen
    menu()
    (width, height) = (950, 600)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    str_to_object(str)
    display_chars()
    index = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ListOfNums[index]:
                    char_objects[index].become_green()
                    index += 1
                else:
                    char_objects[index].become_red()
            display_chars()

            if event.type == pygame.QUIT:
                running = False


main()





