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
beats = 8
instruments = 6

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

    # music controllers

    # hi hat
    hi_hat_text = label_font.render("Hi Hat", True, white)
    screen.blit(hi_hat_text, (30, 30))

    # Snare
    snare_text = label_font.render("Snare", True, white)
    screen.blit(snare_text, (30, 130))

    # Kick/base
    kick_text = label_font.render("Bass", True, white)
    screen.blit(kick_text, (30, 230))

    # Crash
    crash_text = label_font.render("Crash", True, white)
    screen.blit(crash_text, (30, 330))

    # Clap
    clap_text = label_font.render("Clap", True, white)
    screen.blit(clap_text, (30, 430))

    # Floor Tom
    floor_text = label_font.render("Floor Tom", True, white)
    screen.blit(floor_text, (30, 530))

    # seperating each controllers with lines
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 1)

    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(
                screen,
                gray,
                [
                    i * ((WIDTH - 200) // beats) + 200,
                    (j * 100),
                    ((WIDTH - 200) // beats),
                    ((HEIGHT - 200) // instruments),
                ],
                3,
                5,
            )

            boxes.append((rect, (i, j)))

    return boxes


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
