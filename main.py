import pygame
from pygame import mixer

pygame.init()  # initialize the pygame

# screen setup

WIDTH = 1400
HEIGHT = 800

# theme colors

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# create the screen

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Indunil MusicBox")
label_font = pygame.font.Font("Roboto-Bold.ttf", 32)

print("Hello")
