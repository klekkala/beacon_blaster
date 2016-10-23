from random import *
from math import *
import pygame
def init(size):
    global Screen
    Screen = size
class Player:
    def __init__(self):
        self.position = [10,10]
        self.speed = [0.0,0.0]
        self.rotation = 0.0
        self.thrust = 0.0075
        self.being_hit = 0
        self.shielded = False
        self.health = 100.0
        self.energy = 100.0
        self.shield_discharge_rate = 0.2
        self.energy_recharge_rate = 0.05
        self.weapon_type = "Plasma Cannon"
        self.fire_direction = "Forwards"
        self.forward_fire_type = "Single Shot"
        self.total_weapon_reload_time = 30
        self.weapon_reloading_time = 0
        self.bomb_reload_time = 100
        self.bullet_damage = 1
        self.bullet_speed = 1
        self.bomb_ammo = 0
        self.TTL = 10


class Asteroid:
    def __init__(self,x=None,y=None,size=None):
        if (x is not None) and (y is not None) and (size is not None):
            self.position = [x,y]
            self.size = size
        else:
            self.position = [randint(0,Screen[0]),randint(0,Screen[1])]
            self.size = randint(1,5)
        self.speed = [choice([-1,1])*randint(0,500)/(1000.0),
                      choice([-1,1])*randint(0,500)/(1000.0)]
        self.stamina = self.size + 1
        self.being_hit = 0
        self.rotation = 0
        self.rotate_speed = choice([-1,1])*(random()+0.5)*0.1
        
    def get_radius(self):
        if   self.size == 5:  return 64.0
        elif self.size == 4:  return 51.0
        elif self.size == 3:  return 38.0
        elif self.size == 2:  return 26.0
        elif self.size == 1:  return 13.0

class Bomb:
    def __init__(self, p, image):
        self.position = [p.position[0] + (-58*cos(radians(p.rotation))),
                         p.position[1] + (-58*sin(radians(p.rotation)))]
        self.image = pygame.transform.rotate(image, p.rotation+90)
        self.width  = (self.image.get_width() )/2.0
        self.height = (self.image.get_height())/2.0
        self.speed = [-cos(radians(p.rotation))+p.speed[0],
                      -sin(radians(p.rotation))+p.speed[1]]
class Bullet:
    def __init__(self, type, loc, speed, target):
        self.time = 0
        self.type = type
        self.speed = speed
        self.pos = loc
        self.targpos = target
class Explosion:
    def __init__(self,type,size,pos):
        self.size = size
        self.type = type
        self.position = pos
        self.frame = 0
