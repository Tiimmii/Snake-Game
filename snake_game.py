import pygame
import time
import random

#initializing pygame
pygame.init()

#setting window height and width
window_width = 600
window_height = 800

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("SNAKE GAME BY TIMMI")

#setting timer
timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10

display_font = pygame.font.SysFont("arial",30,"bold")
score_font = pygame.font.SysFont("arial",45,"bold")