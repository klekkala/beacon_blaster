 #!/usr/bin/python
import sys
import pygame
pygame.init()
size=width, height=1280, 720
speed=[1,1]
color=1,1,1
screen=pygame.display.set_mode(size)
ball=pygame.image.load('ball.gif')
ballAction=ball.get_rect()
while True:
	  for event in pygame.event.get():
		  if event.type == pygame.QUIT: sys.exit()

	  ballAction = ballAction.move(speed)
	  if ballAction.left < 0 or ballAction.right > width:
	   	speed[0] = -speed[0]
	  if ballAction.top < 0 or ballAction.bottom > height:
		  speed[1] = -speed[1]

	  screen.fill(color)
	  screen.blit(ball, ballAction)
	  pygame.display.flip()
