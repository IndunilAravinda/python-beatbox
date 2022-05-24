from pickle import TRUE
from turtle import color
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
green = (0, 184, 80)
gold = (212, 175, 55)
blue = (0, 255, 255)

# create the screen

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Indunil MusicBox")
label_font = pygame.font.Font("Roboto-Bold.ttf", 32)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boes = []

# matrix like representation of the beatmaker with clicks
clicked = [
    [-1 for _ in range(beats)] for _ in range(instruments)
]  # -1 is not active & 1 is active

bpm = 240
playing = True
active_length = 0
active_beat = 1
beat_changed = True


# main game


def draw_grid(clicks, beat):

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
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green

            rect = pygame.draw.rect(
                screen,
                color,
                [
                    i * ((WIDTH - 200) // beats) + 200,
                    (j * 100) + 5,
                    ((WIDTH - 200) // beats) - 10,
                    ((HEIGHT - 200) // instruments) - 10,
                ],
                0,
                5,
            )

            pygame.draw.rect(
                screen,
                gold,
                [
                    i * ((WIDTH - 200) // beats) + 200,
                    (j * 100),
                    ((WIDTH - 200) // beats),
                    ((HEIGHT - 200) // instruments),
                ],
                5,
                5,
            )

            pygame.draw.rect(
                screen,
                background_color,
                [
                    i * ((WIDTH - 200) // beats) + 200,
                    (j * 100),
                    ((WIDTH - 200) // beats),
                    ((HEIGHT - 200) // instruments),
                ],
                2,
                5,
            )

            boxes.append((rect, (i, j)))

        active = pygame.draw.rect(
            screen,
            blue,
            [
                beat * ((WIDTH - 200) // beats) + 200,
                0,
                ((WIDTH - 200) // beats),
                instruments * 100,
            ],
            5,
            3,
        )

    return boxes


run = True

while run:
    timer.tick(fps)
    screen.fill(background_color)  # background color
    boxes = draw_grid(clicked, active_beat)

    # pygame event handling
    for event in pygame.event.get():

        # quit game
        if event.type == pygame.QUIT:
            run = False

        # click instrument boxes
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][
                        coords[0]
                    ] *= (
                        -1
                    )  # if it is active, then deactivates, and if it is not active then lick will activate

    beat_length = (fps * 60) // bpm

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()

pygame.quit()

print("Hello")
