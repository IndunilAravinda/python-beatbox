from pickle import TRUE
import pygame
from pygame import mixer

pygame.init()  # initialize the pygame

# screen setup

WIDTH = 1400
HEIGHT = 800

# theme colors

black = (0, 0, 0)
background_color = (19, 26, 46)
white = (255, 255, 255)
gray = (65, 78, 115)

# create the screen

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Indunil MusicBox")
label_font = pygame.font.Font("Roboto-Bold.ttf", 32)

fps = 60
timer = pygame.time.Clock()

# main game


def draw_grid():

    # left menu
    left_box = pygame.draw.rect(
        screen, gray, [0, 0, 200, HEIGHT - 200], 3
    )  # left menu rectangle with 0,0 cordinate & 200 width

    # bottom nemu
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 3)
    boxes = []
    colors = [gray, white, gray]


run = True

while run:
    timer.tick(fps)
    screen.fill(background_color)  # background color
    draw_grid()

    # pygame event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()

print("Hello")
