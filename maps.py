import pygame
import random
import color

class Door():
    def __init__(self, host_room, transfer_room, orientation):
        self.host_room = host_room
        self.transfer_room = transfer_room
        self.orientation = orientation

        self.rect = (0, 0, 0, 0)

        if self.orientation == 0:
            self.rect = (500, 100, 200, 25)
        elif self.orientation == 1:
            self.rect = (100, 350, 25, 200)
        elif self.orientation == 2:
            self.rect = (500, 775, 200, 25)
        elif self.orientation == 3:
            self.rect = (1075, 350, 25, 200)

    def draw(self, surface):
        pygame.draw.rect(surface, color.BLACK, self.rect)

    def update(self, events, player):
        pass


class Room():
    def __init__(self, doors = []):
        self.rect = (100, 100, 1000, 700)

        self.doors = doors
        self.rooms = [None, None, None, None]

        self.floor_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, surface):
        pygame.draw.rect(surface, self.floor_color, self.rect)

    def update(self, events):
        pass


class Map():
    def __init__(self, rooms = []):
        self.rooms = rooms

    def draw(self, surface):
        pass

    def update(self, events):
        pass