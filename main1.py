#!/usr/bin/python

import sys, pygame, pygame.mixer

#import bge 
from pygame.locals import *
pygame.init()


sound0 = pygame.mixer.Sound('Laser-SoundBible.com-602495617.wav')
sound = pygame.mixer.Sound('Laser_Cannon-Mike_Koenig-797224747.wav')

#sound0.play()

size = width,height = 1280,720
black = 0,0,0

screen = pygame.display.set_mode(size)

bg = pygame.image.load('bg.jpg')

bg = pygame.transform.scale(bg,size)

bomb = pygame.image.load('b.png')

bomb = pygame.transform.scale(bomb,(25,25))

b1 = pygame.image.load('beacon.png')
 
b1 = pygame.transform.scale(b1,(20,20))
b2 = pygame.image.load('beacon.png')
b4 = pygame.image.load('beacon.png')
b3 = pygame.image.load('beacon.png')

b3 = pygame.transform.scale(b3,(50,50))
b2 = pygame.transform.scale(b2,(50,50))
b4 = pygame.transform.scale(b2,(50,50))

x =0
y =0
r =0


mx,my = pygame.mouse.get_pos()

while 1:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                        sys.exit()
                elif event.type == KEYDOWN and event.key == K_q:
                        sys.exit()
          
                elif event.type ==  MOUSEBUTTONDOWN:
                        sound.play()
                        mx,my = pygame.mouse.get_pos()
       #                 b1.visible = False
                elif event.type == KEYDOWN and event.key == K_SPACE:
                        pygame.image.save(screen,'screenshot.jpg')
                  
        screen.fill((r,0,0))
        screen.blit(bg,(0,0))
        screen.blit(b1,(175,100))
        screen.blit(b2,(375,100))
        screen.blit(b3,(175,300))
        screen.blit(b4,(375,300))
        screen.blit(bomb,(mx-0,my-0))
        pygame.display.flip()
        x= x+1
        y = y+1
        
