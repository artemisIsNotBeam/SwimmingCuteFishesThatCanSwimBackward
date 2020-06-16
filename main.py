import pygame
from pygame.locals import *
import sys

pygame.init()
screenInfo = pygame.display.Info()

#set the width and height of the screen
screenSize = (width, height) = (int(screenInfo.current_w)), (int(screenInfo.current_h))
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

color = (0,127, 255)

def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    pygame.display.flip()

if __name__ == '__main__':
  main()

