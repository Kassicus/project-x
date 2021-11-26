import pygame
import random

import color
import bullet
import maps

bullets = maps.starting_map.active_room.bullet_group

class Chaser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = random.randint(100, 1100)
        self.y = random.randint(100, 800)

        self.width = 15
        self.height = 15

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color.red)

        self.move_x = 0
        self.move_y = 0

        self.speed = 3

        self.rect = (self.x, self.y)

    def update(self, events, player_pos):
        self.rect = (self.x, self.y)

        self.x += self.move_x
        self.y += self.move_y

        self.chase_player(player_pos)
        self.check_bullet_collision()

    def chase_player(self, player_pos):
        if self.x < player_pos[0] - 3:
            self.move_x = self.speed
        elif self.x > player_pos[0] + 3:
            self.move_x = -self.speed
        else:
            self.move_x = 0

        if self.y < player_pos[1] - 3:
            self.move_y = self.speed
        elif self.y > player_pos[1] + 3:
            self.move_y = -self.speed
        else:
            self.move_y = 0

    def check_bullet_collision(self):
        global bullets

        for bullet in bullets:
            if self.x < bullet.x < self.x + self.width:
                if self.y < bullet.y < self.y + self.height:
                    self.kill()
                    bullet.kill()

def spawn_enemies(count, active_map):
    for e in range(count):
        e = Chaser()
        active_map.enemy_group.add(e)
