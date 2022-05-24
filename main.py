from pickle import TRUE
from turtle import back, color
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
medium_font = pygame.font.Font("Roboto-Bold.ttf", 24)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boes = []

# matrix like representation of the beatmaker with clicks
clicked = [
    [-1 for _ in range(beats)] for _ in range(instruments)
]  # -1 is not active & 1 is active

active_list = [1 for _ in range(instruments)]

bpm = 240
playing = True
active_length = 0
active_beat = 1
beat_changed = True


# main game

# configure with sounds

hi_hat = mixer.Sound("sounds\hi hat.WAV")
clap = mixer.Sound("sounds\clap.WAV")
crash = mixer.Sound("sounds\crash.WAV")
kick = mixer.Sound("sounds\kick.WAV")
snare = mixer.Sound("sounds\snare.WAV")
tom = mixer.Sound("sounds\\tom.WAV")

pygame.mixer.set_num_channels(instruments * 3)

# playing beats function


def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()


# UI of the beatbox


def draw_grid(clicks, beat, actives):

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
    hi_hat_text = label_font.render("Hi Hat", True, colors[actives[0]])
    screen.blit(hi_hat_text, (30, 30))

    # Snare
    snare_text = label_font.render("Snare", True, colors[actives[1]])
    screen.blit(snare_text, (30, 130))

    # Kick/base
    kick_text = label_font.render("Bass", True, colors[actives[2]])
    screen.blit(kick_text, (30, 230))

    # Crash
    crash_text = label_font.render("Crash", True, colors[actives[3]])
    screen.blit(crash_text, (30, 330))

    # Clap
    clap_text = label_font.render("Clap", True, colors[actives[4]])
    screen.blit(clap_text, (30, 430))

    # Floor Tom
    floor_text = label_font.render("Floor Tom", True, colors[actives[5]])
    screen.blit(floor_text, (30, 530))

    # seperating each controllers with lines
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 1)

    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                if actives[j] == 1:
                    color = green
                else:
                    color = background_color

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
    boxes = draw_grid(clicked, active_beat, active_list)

    # bottom menu

    play_pause = pygame.draw.rect(screen, gray, [50, HEIGHT - 150, 200, 100], 0, 5)
    play_text = label_font.render("Play/Pause", True, white)
    screen.blit(play_text, (70, HEIGHT - 130))

    if playing:
        play_text2 = medium_font.render("Playing", True, green)
    else:
        play_text2 = medium_font.render("Paused", True, green)

    screen.blit(play_text2, (70, HEIGHT - 100))

    # bpm adjust
    bpm_rect = pygame.draw.rect(screen, gray, [300, HEIGHT - 150, 200, 100], 5, 5)
    bpm_text = medium_font.render("Beats per Minute", True, white)
    screen.blit(bpm_text, (308, HEIGHT - 130))
    bpm_num = label_font.render(f"{bpm}", True, green)
    screen.blit(bpm_num, (370, HEIGHT - 100))

    bpm_add_rect = pygame.draw.rect(screen, gray, [510, HEIGHT - 150, 48, 48], 0, 5)
    bpm_sub_rect = pygame.draw.rect(screen, gray, [510, HEIGHT - 100, 48, 48], 0, 5)
    add_text = medium_font.render("+5", True, white)
    sub_text = medium_font.render("-5", True, white)
    screen.blit(add_text, (520, HEIGHT - 140))
    screen.blit(sub_text, (520, HEIGHT - 90))

    # beats adjust
    beats_rect = pygame.draw.rect(screen, gray, [600, HEIGHT - 150, 200, 100], 5, 5)
    beats_text = medium_font.render("Beats Loop", True, white)
    screen.blit(beats_text, (638, HEIGHT - 130))
    beats_text2 = label_font.render(f"{beats}", True, green)
    screen.blit(beats_text2, (690, HEIGHT - 100))

    beats_add_rect = pygame.draw.rect(screen, gray, [810, HEIGHT - 150, 48, 48], 0, 5)
    beats_sub_rect = pygame.draw.rect(screen, gray, [810, HEIGHT - 100, 48, 48], 0, 5)
    add_text2 = medium_font.render("+1", True, white)
    sub_text2 = medium_font.render("-1", True, white)
    screen.blit(add_text2, (820, HEIGHT - 140))
    screen.blit(sub_text2, (820, HEIGHT - 90))

    # Indunil Aravinda Coded
    welcome_rect = pygame.draw.rect(screen, gray, [900, HEIGHT - 150, 450, 100], 5, 5)
    indunil_aravinda = label_font.render("Indunil's BEATbox", True, green)
    screen.blit(indunil_aravinda, (1010, HEIGHT - 120))

    # instruments selection
    instruments_rects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i * 100), (200, 100))
        instruments_rects.append(rect)

    # play beats accordingly
    if beat_changed:
        play_notes()
        beat_changed = False

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
        # play pause button
        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True
            elif bpm_add_rect.collidepoint(event.pos):
                bpm += 5
            elif bpm_sub_rect.collidepoint(event.pos):
                bpm -= 5
            elif beats_add_rect.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):
                    clicked[i].append(-1)

            elif beats_sub_rect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)

            for i in range(len(instruments_rects)):
                if instruments_rects[i].collidepoint(event.pos):
                    active_list[i] *= -1

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
