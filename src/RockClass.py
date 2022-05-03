import pygame
import random
import time
import math

pygame.init()

display_width = 600
display_height = 500
screen = pygame.display.set_mode( (display_width, display_height) )
fps = 60
font_ubuntumono = pygame.font.SysFont('ubuntumono', 50, True)
rock = pygame.image.load('cave-painting.png').convert_alpha()
rock_width = rock.get_width()
rock_height = rock.get_height()
player = pygame.image.load('wizard.png').convert_alpha()

def initialize():
    global speed_rock, rocks, playerX, playerY
    speed_rock = 2
    playerX = display_width//2
    playerY = 400
    rocks = []
    rocks.append( RockClass() )

class RockClass:
    def __init__(self):
        self.x = display_width//2
        self.y = 0

    def continueDraw(self, a, b):
        self.x += **???**
        self.y += speed_rock
        screen.blit( rock, (self.x, self.y) )

    def collision(self, player, playerX, playerY):
        tolerability = 5
        right_player = playerX + player.get_width() - tolerability
        left_player = playerX + tolerability
        up_player = playerY + tolerability
        right_rock = self.x + rock_width
        left_rock = self.x
        down_rock = self.y + rock_height

        #check collision
        if down_rock > up_player and 
           ( ( left_player < left_rock and left_rock < right_player) or 
               ( right_player > right_rock and right_rock > left_player) ):
            #delete the rock from the screen
            self.x = 5000

initialize()

def update():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

def drawThings():
    #draw background
    screen.fill ( (255, 255, 255) )

    #draw rocks
    for rock2 in rocks:
        rock2.continueDraw(210, 210)

    #draw the player
    screen.blit( player, (playerX, playerY) )

running = True
#main loop
while running:

    #event loop
    for event in pygame.event.get():

        #move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= 30
            if event.key == pygame.K_RIGHT:
                playerX += 30

        #quit
        if event.type == pygame.QUIT:
            running = False

    #to generate infinite rocks
    if rocks[-1].y > 10:
        rocks.append( RockClass() )

    #check the player-rock collision
    for rock2 in rocks:
        rock2.collision(player, playerX, playerY)

    #bordo alto
    if playerX <= 0:
        playerX = 0
    if playerX >= 600:
        playerX = 600

    #update screen
    drawThings()
    update()