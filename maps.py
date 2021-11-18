import pygame
import random
import color

class Room():
    def __init__(self, doors = []):
        self.rect = (100, 100, 1000, 700)

        self.doors = doors

        self.floor_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, surface):
        pygame.draw.rect(surface, self.floor_color, self.rect)

        self.draw_doors(surface)

    def draw_doors(self, surface):
        if self.doors[0] == 1:
            pygame.draw.rect(surface, color.BLACK, (self.rect[0] + 400, self.rect[1], 200, 25))

        if self.doors[1] == 1:
            pygame.draw.rect(surface, color.BLACK, (self.rect[0], self.rect[1] + 250, 25, 200))
        
        if self.doors[2] == 1:
            pygame.draw.rect(surface, color.BLACK, (self.rect[0] + 400, self.rect[1] + self.rect[3] - 25, 200, 25))

        if self.doors[1] == 1:
            pygame.draw.rect(surface, color.BLACK, (self.rect[0] + self.rect[2] - 25, self.rect[1] + 250, 25, 200))

    def update(self, events):
        pass


class Map():
    def __init__(self):
        self.room_0 = Room(doors=[1, 0, 1, 0])
        self.room_1 = Room(doors=[0, 1, 0, 1])

        self.active_room = self.room_0

    def draw(self, surface):
        self.active_room.draw(surface)

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.active_room = self.room_1
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.active_room = self.room_0