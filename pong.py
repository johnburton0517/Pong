# Written by John Burton

import pygame
import random
import time


pygame.init()

X = 600
Y = 600
window = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window.fill(BLACK)

# object current co-ordinates
player1X = 580
player1Y = 200

player2X = 0
player2Y = 200
  
# dimensions of the paddle 
width = 20
height = 100


paddleVel = 8

ball_x = 300
# ball_y = 300
ball_y = random.randint(150, 450)
radius = 12

hitBottom = False
list = [True, False]
moveRight = random.choice(list)
# moveRight = True

player1Score = 0
player2Score = 0

# text
font = pygame.font.SysFont('chalkduster.ttf', 40)
player1Text = font.render(('Player 1: ' + str(player1Score)), True, WHITE)
player2Text = font.render(('Player 2: ' + str(player2Score)), True, WHITE)
textRect1 = player1Text.get_rect()
textRect2 = player1Text.get_rect()
textRect1.center = (500, 25)
textRect2.center = (100, 25)

font2 = pygame.font.SysFont('chalkduster.ttf', 500)
gameOverText = font.render("GAME OVER!", True, WHITE)
textRect3 = gameOverText.get_rect()
textRect3.center = (300, 200)

playerWinText = font.render("", True, WHITE)
textRect4 = playerWinText.get_rect()
textRect4.center = (185, 300)

isRunning = True

while isRunning:

    ticks=pygame.time.get_ticks()
    
    pygame.time.delay(10)

    # exit the game
    events = pygame.event.get()
    # exit the game
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    ###### Key Presses ######

    # stores keys pressed 
    keys = pygame.key.get_pressed()
         
    # if up arrow key is pressed   
    if keys[pygame.K_UP] and player1Y>0:
          
        # decrement in y co-ordinate
        player1Y -= paddleVel
          
    # if down arrow key is pressed   
    if keys[pygame.K_DOWN] and player1Y<Y - height:
        # increment in y co-ordinate
        player1Y += paddleVel

    # if W  key is pressed
    if keys[pygame.K_w] and player2Y>0:
          
        # decrement in x co-ordinate
        player2Y -= paddleVel
          
    # if S  key is pressed
    if keys[pygame.K_s] and player2Y<Y - height:
          
        # increment in x co-ordinate
        player2Y += paddleVel

    ###########################



    ###### Ball Movement ######

    if moveRight == True:
        ball_x += 2 + (ticks * .00005)
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius, 0)

    if moveRight == False:
        ball_x -= (2 + (ticks * .00005))
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius, 0)

    # move down
    if hitBottom == False:
        ball_y += 2 + (ticks * .00005)
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius, 0)

        if ball_y >= 600 - radius:
            hitBottom = True

    # move up
    if hitBottom == True:
        ball_y -= (2 + (ticks * .00005))
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius, 0)

        if ball_y <= radius:
            hitBottom = False


    # hit right paddle
    if ball_x >= player1X - radius and  ball_y >= player1Y + radius and ball_y < player1Y + height + radius:
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius, 0)
        moveRight = False

    # hit left paddle
    if ball_x <= player2X + width and  ball_y <= player2Y + height - radius and ball_y > player2Y - radius:
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius, 0)
        moveRight = True
        

    # Points Scored
    # ball hits right side
    if ball_x >= 600 - radius:
        time.sleep(.75)
        ball_x = 300
        # ball_y = 300
        ball_y = random.randint(150, 450)
        list = [True, False]
        moveRight = random.choice(list)
        player2Score += 1
        player2Text = font.render(('Player 2: ' + str(player2Score)), True, WHITE)


    # ball hits left side
    if ball_x <= radius:
        time.sleep(.75)
        ball_x = 300
        # ball_y = 300
        ball_y = random.randint(150, 450)
        list = [True, False]
        moveRight = random.choice(list)
        player1Score += 1
        player1Text = font.render(('Player 1: ' + str(player1Score)), True, WHITE)



    ###########################
    
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player1X, player1Y, width, height))
    pygame.draw.rect(window, WHITE, (player2X, player2Y, width, height))
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), radius, 0)

    # Text display
    window.blit(player1Text, textRect1)
    window.blit(player2Text, textRect2)
    
    pygame.display.update()

    # Game Over
    if player1Score == 5:
        playerWinText = font.render("Player One Wins!", True, WHITE)
        while True:
            # exit the game
            events = pygame.event.get()
            # exit the game
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            window.fill(BLACK)
            window.blit(gameOverText, textRect3)
            window.blit(playerWinText, textRect4)
            pygame.display.update()
    elif player2Score == 5:
        playerWinText = font.render("Player Two Wins!", True, WHITE)
        while True:
            # exit the game
            events = pygame.event.get()
            # exit the game
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            window.fill(BLACK)
            window.blit(gameOverText, textRect3)
            window.blit(playerWinText, textRect4)
            pygame.display.update()

