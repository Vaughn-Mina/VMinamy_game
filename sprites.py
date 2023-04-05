import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
from random import random
import random

vec = pg.math.Vector2

# player class

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        # if keystate[pg.K_w]:
        #     self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        # if keystate[pg.K_s]:
        #     self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
            # allows the player to move a set distance that acts like a dash
        if keystate[pg.K_LCTRL]:
            if keystate[pg.K_d]:
                self.pos.x += DASHDISTANCE
                print("I dashed to the right")
            if keystate[pg.K_a]:
                self.pos.x -= DASHDISTANCE
                print("I dashed to the left")
            if keystate[pg.K_w]:
                self.pos.y -= DASHDISTANCE
                print("I dashed upwards")
            if keystate[pg.K_s]:
                self.pos.y += DASHDISTANCE
                print("I dashed downwards")
        # if keystate[pg.K_LALT]:

        # if keystate[pg.K_p]:
        #     if PAUSED == False:
        #         PAUSED = True
        #         print(PAUSED)
        #     else:
        #         PAUSED = False
        #         print(PAUSED)
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
    
    def inbounds(self):
        if self.rect.x > WIDTH - 50:
            self.pos.x = WIDTH - 25
            self.vel.x = 0
            print("i am off the right side of the screen...")
        if self.rect.x < 0:
            self.pos.x = 25
            self.vel.x = 0
            print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            print("i am off the bottom of the screen")
        if self.rect.y < 0:
            print("i am off the top of the screen...")
    def mob_collide(self):
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                print("you collided with an enemy...")
                self.game.score += 1
                print(SCORE)
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # ...
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos
    def dash(self):


        # for rng in range():
        #     rng = random.randint(0,100)
        #     if rng <=25:
        #         self.pos.x += MOB_DASH
        #         print("Mob dashed positive x")
        #     if rng >=25 and rng <=40:
        #         self.pos.x -= MOB_DASH 
        #         print("Mob dashed negative x")


        # movement_choices = {"dash left", "dash right", "dash up", "dash down"}
        # Mob_decision = movement_choices[randint(0,3)]
        # if Mob_decision == "dash left":
        #     self.pos.x -= MOB_DASH
        #     print("the mob has dashed to the left")
        # if Mob_decision == "dash right":
        #     self.pos.x += MOB_DASH
        #     print("the mob has dashed to the right")
        # if Mob_decision == "dash up":
        #     self.pos.y -= MOB_DASH
        #     print("the mob has dashed upwards")
        # if Mob_decision == "dash down":
        #     self.pos.y += MOB_DASH
        #     print("the mob has dashed downwards")
# create a new platform class...

class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant