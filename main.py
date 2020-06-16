import pygame
import random
from pygame.locals import *
import sys

pygame.init()
screenInfo = pygame.display.Info()

#set the width and height of the screen
screenSize = (width, height) = (int(screenInfo.current_w)), (int(screenInfo.current_h))
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

color = (0,127, 255)

fish = pygame.image.load("fish.png")
fish = pygame.transform.smoothscale(fish,(80,80))
fishRect =  fish.get_rect()
fishRect.center = (width//2, height//2)

speed = pygame.math.Vector2(0,10)
rotation = random.randint(0,360)
speed.rotate_ip(rotation)
fish = pygame.transform.rotate(fish, 180-rotation)

def moveFish():
  fishRect.move_ip(speed)

def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    screen.blit(fish, fishRect)
    pygame.display.flip()
    moveFish()

if __name__ == '__main__':
  main()

