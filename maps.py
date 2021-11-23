import pygame

import color
import random

class Door():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, surface):
        pygame.draw.rect(surface, color.black, (self.x, self.y, self.width, self.height))

    def update(self, events):
        pass

class Room():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 1000
        self.height = 700

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.doors = []

        self.top_door = Door(self.x + 400, self.y, 200, 25)
        self.bottom_door = Door(self.x + 400, self.y + self.height - 25, 200, 25)
        self.left_door = Door(self.x, self.y + 250, 25, 200)
        self.right_door = Door(self.x + self.width - 25, self.y + 250, 25, 200)

        self.doors.extend((self.top_door, self.bottom_door, self.left_door, self.right_door))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

        for door in self.doors:
            door.draw(surface)

    def update(self, events):
        for door in self.doors:
            door.update(events)

class Map():
    def __init__(self):
        self.rooms = []
        self.active_room = None

    def draw(self, surface):
        if self.active_room != None:
            self.active_room.draw(surface)

    def update(self, events):
        if self.active_room != None:
            self.active_room.update(events)

starting_map = Map()

room_1 = Room()
room_2 = Room()
room_3 = Room()

starting_map.rooms.extend((room_1, room_2, room_3))

starting_map.active_room = starting_map.rooms[0]