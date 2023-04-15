import pygame
import time
import random

#initializing pygame
pygame.init()

#setting window height and width
window_width = 480
window_height = 720

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("SNAKE GAME BY TIMMII")

#setting timer
timer = pygame.time.Clock()

snake_speed = 10

#default position of the snake
snake_position = [100, 50]
#defining first four blocks of the snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]
#the initial food position should apear randomly anywhere within the window_width and window_height
food_position = [random.randrange(1, (window_width//10))*10,
                 random.randrange(1, (window_height//10))*10
                 ]
food_spawn = False #determines whether food should spawn or not
score = 0 #initial score

# setting default snake direction towards left
direction = 'LEFT'
change_to = direction