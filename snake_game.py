import pygame
import time
import random

window_width = 720
window_height = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#initializing pygame
pygame.init()

#setting window height and width

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("SNAKE GAME BY TIMMII")

#setting timer
timer = pygame.time.Clock()

snake_speed = 15

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

# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

#displaying the scores
def show_scores(font, size, color):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Your score is: '+str(score)+"         press Q to quit", True, color)
    score_surface_rect = score_surface.get_rect()
    window.blit(score_surface, score_surface_rect)

#on game over
def game_over():
    file = open("highest-score.txt", "r+")
    for line in file:
        if score > int(line):
            line = score
        font = pygame.font.SysFont("arial", 20)
        font_surface = font.render("You snooze you loose Score: "+str(score)+" high score: "+str(line), True, red)
        font_surface_rect = font_surface.get_rect()
    
    #setting the position of the rectangle to the middle
    font_surface_rect.midtop = (window_width/2, window_height/4)

    window.blit(font_surface, font_surface_rect)
    pygame.display.flip()

    #quit the program after five seconds
    time.sleep(2)
    #quit pygame
    pygame.quit()
    #quit the program
    quit()

#if key Q is pressed game should automatically quit
def quit_game():
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit_game()
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to ="LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
    
    #To prevent snake from moving in the opposite direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    #moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    
    #snake growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score+=1
        food_spawn = True
        snake_speed+=1
    else:
        snake_body.pop()

    if food_spawn:
        food_position = [ random.randrange(1, (window_width//10))*10,
                          random.randrange(1, (window_height//10))*10]
    food_spawn = False
    window.fill(black)
    #drawing the snake and food
    #drawing the snake
    for position in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(position[0], position[1], 10, 10))
    #drawing the food
    pygame.draw.rect(window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))
    
    #game over conditions
    if snake_position[0] < 0 or snake_position[0] >=window_width:
        game_over()
    if snake_position[1] < 0 or snake_position[1] >=window_height:
        game_over()
    
    #snake touching its body
    for pos in snake_body[1:]:
        if pos[0] == snake_position[0] and pos[1] == snake_position[1]:
            game_over()
    
    #displaying the score continously
    show_scores("times new roman", 20, blue)
    #refreshing the game
    pygame.display.update()
    #fps timer
    timer.tick(snake_speed)

    
    
    



