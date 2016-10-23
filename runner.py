##import psyco
##psyco.full()
import pygame,sys,pygame.mixer
from pygame.locals import *
import os, sys
from math import *
import random
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

Screen = (1300,720)
size = width,height = 1280,720
screen = pygame.display.set_mode(size)

#b = pygame.image.load('space.png')

pygame.display.set_caption("Beacon Blaster")
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
Surface = pygame.display.set_mode(Screen)
#bg = pygame.image.load('b.jpg')
#bg = pygame.transform.scale(bg,size)
Explosions = []
Asteroids = []
Bullets = []
Bombs = []

Level = 0
blast_radius = 100
Font  = pygame.font.SysFont("Times New Roman",  8)
Font2 = pygame.font.SysFont("Times New Roman", 10)
Font3 = pygame.font.SysFont("Times New Roman", 16)

Clock = pygame.time.Clock()
TargetFPS = 50.0 #200.0, 100.0, 50.0, 25.0, 13.0
IdealFPS = 200.0

import Classes, Images, MenuItem, GameMenu

Classes.init(Screen)
# Creating the screen


p1 = Classes.Player()
p1.TTL = 10
a = Classes.Asteroid(400,400, 3)
Asteroids.append(Classes.Asteroid(200,200, 1))
Asteroids.append(Classes.Asteroid(200,300, 1))
Asteroids.append(Classes.Asteroid(300,200, 2))
Asteroids.append(Classes.Asteroid(300,300, 1))
Asteroids.append(Classes.Asteroid(300,400, 1))
Asteroids.append(Classes.Asteroid(600,600, 1))
Asteroids.append(Classes.Asteroid(600,620, 1))
Asteroids.append(Classes.Asteroid(650,200, 1))
Asteroids.append(Classes.Asteroid(100,600, 1))
Asteroids.append(Classes.Asteroid(800,100, 1))
Asteroids.append(Classes.Asteroid(900,400, 1))
Asteroids.append(Classes.Asteroid(950,300, 1))
Asteroids.append(Classes.Asteroid(1200,200, 1))
Asteroids.append(Classes.Asteroid(1150,100, 1))
Asteroids.append(Classes.Asteroid(100,600, 1))
Asteroids.append(Classes.Asteroid(1000,700, 1))
Asteroids.append(a)
Asteroids.append(Classes.Asteroid(500,400, 1))

Explosions.append(Classes.Explosion("Asteroid",a.size,a.position))

#def StartScreen():

    #menu_items = ('Start', 'Quit')
    #funcs = {'Start': main,
             #'Quit': sys.exit}
    #gm = GameMenu.GameMenu(Surface, funcs.keys(), funcs)

    #pygame.display.set_caption('Game Menu')

    #gm.run()

def Fire(target_pos, speed):
    bull = Classes.Bullet("Plasma", p1.position, 0.5, target_pos)
    slope = (target_pos[1]-p1.position[1])/(target_pos[0]-p1.position[0])
    bull.pos = p1.position
    Bullets.append(bull)
    old_x = p1.position[0]
    old_y = p1.position[1]
    for x in xrange(540):
        for b in Bullets:
            new_x = old_x + b.speed
            new_y = old_y + slope*(b.speed)
            p1.position = [new_x, new_y]
            old_x = new_x
            old_y = new_y
            Draw()

def GetInput():
    key = pygame.key.get_pressed()
    button = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or key[K_ESCAPE]:
            pygame.quit(); sys.exit()
    if key[K_SPACE] and button[0]:
        p1.shielded = True
        target_pos = pygame.mouse.get_pos()
        Fire(target_pos, 0.2)
        
    if key[K_b]:
        if p1.bomb_reload_time == 100 and p1.bomb_ammo >= 1:
            Bombs.append(Classes.Bomb(p1,Images.BombImage))
            p1.bomb_ammo -= 1
            p1.bomb_reload_time = 0
    if key[K_s]:
        p1.shielded = True

    if button[0]:
        p1.TTL = p1.TTL-1
        loc = pygame.mouse.get_pos()
        p1.position[0] = loc[0]
        p1.position[1] = Screen[1]-loc[1]

    pygame.event.wait()

def BreakAsteroid():
    #global Level, a, Explosions
    explo_astro = []
    for a in Asteroids:
        val = sqrt( (p1.position[0] - a.position[0])**2 + (p1.position[1] - a.position[1])**2)
        print val
        if val < blast_radius:
            print 99
            Explosions.append(Classes.Explosion("Asteroid",a.size,a.position))
            explo_astro.append(a)

    for x in xrange(150):
        Update()
        Draw()

    for a in explo_astro:
        Asteroids.remove(a)


def Die():
    global Level, Asteroids, Explosions, p1
    Explosions.append(Classes.Explosion("Self", 1, p1.position))
    p1.speed = [0.0,0.0]
    for x in xrange(540):
        Update()
        Draw()
    #p1 = Classes.Player()
    #Level = 0
    #Asteroids = []
    #Explosions = []


def Update():
    #Self
    if p1.weapon_reloading_time > 0: p1.weapon_reloading_time -= 1
    else: p1.weapon_reloading_time = 0
    if p1.bomb_reload_time < 100: p1.bomb_reload_time += 0.25
    else: p1.bomb_reload_time = 100
    if p1.shielded: p1.energy -= p1.shield_discharge_rate
    p1.energy += float(p1.energy_recharge_rate)
    if p1.energy > 100.0: p1.energy = 100.0
    if p1.being_hit > 0: p1.being_hit -= 1
    #Bullets
    for b in Bullets:
        b.time += 1
        if b.time > 300:
            Bullets.remove(b)
    #Asteroids
    for a in Asteroids:
        a.rotation += a.rotate_speed
        if   a.rotation >  360.0: a.rotation -= 360.0
        elif a.rotation < -360.0: a.rotation += 360.0
        if a.being_hit > 0: a.being_hit -= 1
        else: a.being_hit = 0

    #Explosions
    for e in Explosions:
        e.frame += 1

def rndint(number):
    return int(round(number))

def Draw():  
    #Clear
    b= pygame.image.load('space.png')
    b= pygame.transform.scale(b,Screen)
    Surface.blit(b,(0,0))
    #Surface.fill((0,0,0))
    #Self
    ToDraw = True
    for e in Explosions:
        if e.type == "Self": ToDraw = False; break
    if ToDraw:
        if not p1.being_hit: ShipImageRotated = pygame.transform.rotozoom(Images.ShipImages[0], p1.rotation, 1.0)
        else:                ShipImageRotated = pygame.transform.rotozoom(Images.ShipImages[1], p1.rotation, 1.0)
        height = ShipImageRotated.get_height()/2.0
        width = ShipImageRotated.get_width()/2.0
        BlitPos = [rndint(p1.position[0]-width),rndint(p1.position[1]+height)]
        Surface.blit(ShipImageRotated,(BlitPos[0],Screen[1]-BlitPos[1]))
        if p1.shielded: Surface.blit(Images.ShieldImage,(p1.position[0]-38,Screen[1]-(p1.position[1]+38)))
    #Bullets
    for b in Bullets:
        if   b.type == "Plasma Cannon": BulletImage = Images.BulletImages[0]
        elif b.type == "Plasma Blast":  BulletImage = Images.BulletImages[1]
        Surface.blit(BulletImage, (rndint(b.position[0]-11), Screen[1]-rndint(b.position[1]+11)))
    #Bombs
    for b in Bombs:
        Surface.blit(b.image, (b.position[0]-b.width, Screen[1]-rndint(b.position[1]+b.height)))
    
    #Asteroids
    for a in Asteroids:
        if not a.being_hit: image = Images.AsteroidImages[4-(a.size-1)]
        else:              image = Images.RedAsteroidImages[4-(a.size-1)]
        image = pygame.transform.rotozoom(image, a.rotation, 1.0)
        Surface.blit(image, (rndint(a.position[0]-(image.get_width()/2.0)), Screen[1]-rndint(a.position[1]+(image.get_height()/2.0))))
    #Explosions
    for e in Explosions:
        try:
            if e.type == "Asteroid":
                index = int(e.frame/4.0)-1
                if index >= 17: raise IndexError
                if   e.size == 5: Surface.blit(Images.Asteroid_Explosion_Frames[index   ], (rndint(e.position[0]-71), rndint(Screen[1]-(e.position[1] + 100))))
                elif e.size == 4: Surface.blit(Images.Asteroid_Explosion_Frames[index+17], (rndint(e.position[0]-54), rndint(Screen[1]-(e.position[1] +  75))))
                elif e.size == 3: Surface.blit(Images.Asteroid_Explosion_Frames[index+34], (rndint(e.position[0]-36), rndint(Screen[1]-(e.position[1] +  50))))
                elif e.size == 2: Surface.blit(Images.Asteroid_Explosion_Frames[index+51], (rndint(e.position[0]-27), rndint(Screen[1]-(e.position[1] +  38))))
                else:             Surface.blit(Images.Asteroid_Explosion_Frames[index+68], (rndint(e.position[0]-18), rndint(Screen[1]-(e.position[1] +  25))))
            if e.type == "Bomb":
                Surface.blit(Images.Bomb_Explosion_Frames[(e.frame/12)-1], (e.position[0]-90, Screen[1]-(e.position[1]+68)))
            if e.type == "Self":
                Surface.blit(Images.Self_Explosion_Frames[e.frame/27], (e.position[0]-128,Screen[1]-(e.position[1]+96)))
        except:
            Explosions.remove(e)
    #HUD: Basic Info.
        #Energy Bar

    #Flip
    pygame.display.flip()


def main():
    #b = pygame.image.load('space.png')
    #Surface.blit(bg,(0,0))
    p1.TTL = 10
    while True:
        GetInput()
        #Update()
        #BreakAsteroid()
        #Die()
        if p1.TTL is 0:
            Die()
            BreakAsteroid()
        Draw()

if __name__ == '__main__': main()
