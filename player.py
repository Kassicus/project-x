import pygame
import color

class Player():
    def __init__(self):
        self.x = 600
        self.y = 450
        
        self.width = 35
        self.height = 35

        self.move_x = 0
        self.move_y = 0

        self.speed = 5

    def draw(self, surface):
        pygame.draw.rect(surface, color.WHITE, (self.x, self.y, self.width, self.height))

    def update(self, events):
        self.x += self.move_x
        self.y += self.move_y

        self.event_handler(events)
        self.check_movement_border()

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.move_x = self.speed
                if event.key == pygame.K_a:
                    self.move_x = -self.speed

                if event.key == pygame.K_s:
                    self.move_y = self.speed
                if event.key == pygame.K_w:
                    self.move_y = -self.speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    self.move_x = 0
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    self.move_y = 0

    def check_movement_border(self):
        if self.x < 100:
            self.x = 100
            self.move_x = 0
        
        if self.x + self.width > 1100:
            self.x = 1100 - self.width
            self.move_x = 0

        if self.y < 100:
            self.y = 100
            self.move_y = 0

        if self.y + self.height > 800:
            self.y = 800 - self.height
            self.move_y = 0