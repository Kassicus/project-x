import pygame

import color

active_bullets = pygame.sprite.Group()

def draw_bullets(surface):
    active_bullets.draw(surface)

def update_bullets():
    active_bullets.update()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, damage, speed, size):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.move_x = 0
        self.move_y = 0

        self.damage = damage

        self.speed = speed
        self.size = size

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(color.red)

        self.rect = (self.x, self.y)

        self.direction = direction

    def update(self):
        self.x += self.move_x
        self.y += self.move_y

        self.rect = (self.x, self.y)

        if self.direction == 'right':
            self.move_x = self.speed
        elif self.direction == 'left':
            self.move_x = -self.speed
        elif self.direction == 'up':
            self.move_y = -self.speed
        elif self.direction == 'down':
            self.move_y = self.speed

        if self.x < -50 or self.x > 1250 or self.y < -50 or self.y > 950:
            self.kill()

class BaseGun():
    def __init__(self):
        self.name = "Base Gun"

        self.damage = 1
        self.max_cooldown = 10
        self.cooldown = self.max_cooldown

        self.bullet_speed = 10
        self.bullet_size = 5

        global active_bullets

    def shoot(self, direction, x, y):
        self.cooldown -= 1

        if self.cooldown <= 0:
            if direction == 'right':
                b = Bullet(x, y, 'right', self.damage, self.bullet_speed, self.bullet_size)   
            elif direction == 'left':
                b = Bullet(x, y, 'left', self.damage, self.bullet_speed, self.bullet_size)
            elif direction == 'up':
                b = Bullet(x, y, 'up', self.damage, self.bullet_speed, self.bullet_size)
            elif direction == 'down':
                b = Bullet(x, y, 'down', self.damage, self.bullet_speed, self.bullet_size)
        
            active_bullets.add(b)

            self.cooldown = self.max_cooldown