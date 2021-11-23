import pygame

import color

class Player():
    def __init__(self):
        self.x = 500
        self.y = 400

        self.radius = 25

        self.move_x = 0
        self.move_y = 0

        self.speed = 5

        self.has_friction_x = True
        self.has_friction_y = True
        
        self.friction = 1

    def draw(self, surface):
        pygame.draw.circle(surface, color.WHITE, (self.x, self.y), self.radius)

    def update(self, events):
        self.x += self.move_x
        self.y += self.move_y

        if self.has_friction_x:
            if self.move_x > 0:
                self.move_x -= self.friction
            elif self.move_x < 0:
                self.move_x += self.friction

        if self.has_friction_y:
            if self.move_y > 0:
                self.move_y -= self.friction
            elif self.move_y < 0:
                self.move_y += self.friction

        self.movement_handler(events)

    def movement_handler(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.move_x = self.speed
                    self.has_friction_x = False
                if event.key == pygame.K_a:
                    self.move_x = -self.speed
                    self.has_friction_x = False

                if event.key == pygame.K_s:
                    self.move_y = self.speed
                    self.has_friction_y = False
                if event.key == pygame.K_w:
                    self.move_y = -self.speed
                    self.has_friction_y = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    self.has_friction_x = True
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    self.has_friction_y = True
