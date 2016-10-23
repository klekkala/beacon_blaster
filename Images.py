import pygame
pygame.init()

size_player = (70, 80)
player = pygame.image.load("Player/Ship.png")
player = pygame.transform.scale(player, size_player)
ShipImages = [player.convert_alpha(),
              pygame.image.load("Player/ShipRed.png").convert_alpha(),
              pygame.image.load("HUD/ShipDisplay.png").convert_alpha()]
BulletImages = [pygame.image.load("Plasma Cannon.png").convert_alpha(),
                pygame.image.load("Plasma Blast.png").convert_alpha()]
HudBomb = [pygame.image.load("HUD/BombImage.png").convert_alpha(),
           pygame.image.load("HUD/BombOutline.png").convert_alpha()]
BombImage = pygame.image.load("Bomb/Bomb.png").convert_alpha()

FireDisplay = [pygame.image.load("HUD/ForwardFire.png").convert_alpha(),
               pygame.image.load("HUD/BackwardFire.png").convert_alpha(),
               pygame.transform.rotate(pygame.image.load("HUD/ForwardFire.png").convert_alpha(), 90),
               pygame.transform.rotate(pygame.image.load("HUD/BackwardFire.png").convert_alpha(), 90)]
BombPowerUpImages = [pygame.image.load("Bomb/Bomb_Power_Up/Bomb.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb2.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb3.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb4.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb5.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb6.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb7.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb8.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb9.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb10.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb11.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb12.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb13.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb14.png").convert_alpha(),
                     pygame.image.load("Bomb/Bomb_Power_Up/Bomb15.png").convert_alpha()]
ShieldImage = pygame.image.load("Player/Shield.png").convert_alpha()

AsteroidImages = [pygame.image.load("Asteroid/Asteroids/Normal/AsteroidVeryLarge.png").convert_alpha(),
                  pygame.image.load("Asteroid/Asteroids/Normal/AsteroidLarge.png").convert_alpha(),
                  pygame.image.load("Asteroid/Asteroids/Normal/AsteroidMedium.png").convert_alpha(),
                  pygame.image.load("Asteroid/Asteroids/Normal/AsteroidSmall.png").convert_alpha(),
                  pygame.image.load("Asteroid/Asteroids/Normal/AsteroidVerySmall.png").convert_alpha()]

RedAsteroidImages = [pygame.image.load("Asteroid/Asteroids/Hit/AsteroidVeryLargeRed.png").convert_alpha(),
                     pygame.image.load("Asteroid/Asteroids/Hit/AsteroidLargeRed.png").convert_alpha(),
                     pygame.image.load("Asteroid/Asteroids/Hit/AsteroidMediumRed.png").convert_alpha(),
                     pygame.image.load("Asteroid/Asteroids/Hit/AsteroidSmallRed.png").convert_alpha(),
                     pygame.image.load("Asteroid/Asteroids/Hit/AsteroidVerySmallRed.png").convert_alpha()]

size = (500, 400)
picture1 = pygame.image.load("Player/Self_Explode/Explode.png")
picture1 = pygame.transform.scale(picture1, size)
picture2 = pygame.image.load("Player/Self_Explode/Explode2.png")
picture2 = pygame.transform.scale(picture2, size)
picture3 = pygame.image.load("Player/Self_Explode/Explode3.png")
picture3 = pygame.transform.scale(picture3, size)
picture4 = pygame.image.load("Player/Self_Explode/Explode4.png")
picture4 = pygame.transform.scale(picture4, size)
picture5 = pygame.image.load("Player/Self_Explode/Explode5.png")
picture5 = pygame.transform.scale(picture5, size)
picture6 = pygame.image.load("Player/Self_Explode/Explode6.png")
picture6 = pygame.transform.scale(picture6, size)
picture7 = pygame.image.load("Player/Self_Explode/Explode7.png")
picture7 = pygame.transform.scale(picture7, size)
picture8 = pygame.image.load("Player/Self_Explode/Explode8.png")
picture8 = pygame.transform.scale(picture8, size)
picture9 = pygame.image.load("Player/Self_Explode/Explode9.png")
picture9 = pygame.transform.scale(picture9, size)
picture10 = pygame.image.load("Player/Self_Explode/Explode10.png")
picture10 = pygame.transform.scale(picture10, size)
picture11 = pygame.image.load("Player/Self_Explode/Explode11.png")
picture11 = pygame.transform.scale(picture11, size)
picture12 = pygame.image.load("Player/Self_Explode/Explode12.png")
picture12 = pygame.transform.scale(picture12, size)
picture13 = pygame.image.load("Player/Self_Explode/Explode13.png")
picture13 = pygame.transform.scale(picture13, size)
picture14 = pygame.image.load("Player/Self_Explode/Explode14.png")
picture14 = pygame.transform.scale(picture14, size)
picture15 = pygame.image.load("Player/Self_Explode/Explode15.png")
picture15 = pygame.transform.scale(picture15, size)
picture16 = pygame.image.load("Player/Self_Explode/Explode16.png")
picture16 = pygame.transform.scale(picture16, size)
picture17 = pygame.image.load("Player/Self_Explode/Explode17.png")
picture17 = pygame.transform.scale(picture17, size)
picture18 = pygame.image.load("Player/Self_Explode/Explode18.png")
picture18 = pygame.transform.scale(picture18, size)
picture19 = pygame.image.load("Player/Self_Explode/Explode19.png")
picture19 = pygame.transform.scale(picture19, size)
picture20 = pygame.image.load("Player/Self_Explode/Explode20.png")
picture20 = pygame.transform.scale(picture20, size)
picture21 = pygame.image.load("Player/Self_Explode/Explode21.png")
picture21 = pygame.transform.scale(picture21, size)
picture22 = pygame.image.load("Player/Self_Explode/Explode22.png")
picture22 = pygame.transform.scale(picture22, size)
picture23 = pygame.image.load("Player/Self_Explode/Explode23.png")
picture23 = pygame.transform.scale(picture23, size)
picture24 = pygame.image.load("Player/Self_Explode/Explode24.png")
picture24 = pygame.transform.scale(picture24, size)
picture25 = pygame.image.load("Player/Self_Explode/Explode25.png")
picture25 = pygame.transform.scale(picture25, size)
picture26 = pygame.image.load("Player/Self_Explode/Explode26.png")
picture26 = pygame.transform.scale(picture26, size)
picture27 = pygame.image.load("Player/Self_Explode/Explode27.png")
picture27 = pygame.transform.scale(picture27, size)

Self_Explosion_Frames = [picture1.convert_alpha(),
                        picture2.convert_alpha(),
                        picture3.convert_alpha(),
                        picture4.convert_alpha(),
                        picture5.convert_alpha(),
                        picture6.convert_alpha(),
                        picture7.convert_alpha(),
                        picture8.convert_alpha(),
                        picture9.convert_alpha(),
                        picture10.convert_alpha(),
                        picture11.convert_alpha(),
                        picture12.convert_alpha(),
                        picture13.convert_alpha(),
                        picture14.convert_alpha(),
                        picture15.convert_alpha(),
                        picture16.convert_alpha(),
                        picture17.convert_alpha(),
                        picture18.convert_alpha(),
                        picture19.convert_alpha(),
                        picture20.convert_alpha(),
                        picture21.convert_alpha(),
                        picture22.convert_alpha(),
                        picture23.convert_alpha(),
                        picture24.convert_alpha(),
                        picture25.convert_alpha(),
                        picture26.convert_alpha(),
                        picture27.convert_alpha()]

Asteroid_Explosion_Frames = [pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode2.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode3.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode4.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode5.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode6.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode7.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode8.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode9.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode10.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode11.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode12.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode13.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode14.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode15.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode16.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode17.png").convert_alpha(), (142, 200)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode2.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode3.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode4.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode5.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode6.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode7.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode8.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode9.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode10.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode11.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode12.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode13.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode14.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode15.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode16.png").convert_alpha(), (107, 150)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode17.png").convert_alpha(), (107, 150)),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode2.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode3.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode4.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode5.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode6.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode7.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode8.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode9.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode10.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode11.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode12.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode13.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode14.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode15.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode16.png").convert_alpha(),
                             pygame.image.load("Asteroid/Asteroid_Explode/Explode17.png").convert_alpha(),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode2.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode3.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode4.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode5.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode6.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode7.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode8.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode9.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode10.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode11.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode12.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode13.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode14.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode15.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode16.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode17.png").convert_alpha(), (54, 75)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode2.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode3.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode4.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode5.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode6.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode7.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode8.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode9.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode10.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode11.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode12.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode13.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode14.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode15.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode16.png").convert_alpha(), (36, 50)),
                             pygame.transform.scale(pygame.image.load("Asteroid/Asteroid_Explode/Explode17.png").convert_alpha(), (36, 50)),]
Bomb_Explosion_Frames = [pygame.image.load("Bomb/Bomb_Explode/Explode.png").convert_alpha(),
                         pygame.image.load("Bomb/Bomb_Explode/Explode2.png").convert_alpha(),
                         pygame.image.load("Bomb/Bomb_Explode/Explode3.png").convert_alpha(),
                         pygame.image.load("Bomb/Bomb_Explode/Explode4.png").convert_alpha(),
                         pygame.image.load("Bomb/Bomb_Explode/Explode5.png").convert_alpha(),
                         pygame.image.load("Bomb/Bomb_Explode/Explode6.png").convert_alpha(),
                         pygame.image.load("Bomb/Bomb_Explode/Explode7.png").convert_alpha(),
                         pygame.image.load("Bomb/Bomb_Explode/Explode8.png").convert_alpha()]