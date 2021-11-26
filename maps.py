import pygame
import random

import color

class Door():
    def __init__(self, x, y, width, height, parent, flow):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.parent = parent

        self.target = None

        self.flow = flow
    
    def draw(self, surface):
        pygame.draw.rect(surface, color.black, (self.x, self.y, self.width, self.height))

    def update(self, events, player):
        if self.x < player.x < self.x + self.width:
            if self.y < player.y < self.y + self.height:
                self.parent.parent.active_room = self.target
                if self.flow == "top":
                    player.x = 600
                    player.y = 700
                elif self.flow == "bottom":
                    player.x = 600
                    player.y = 200
                elif self.flow == "left":
                    player.x = 1000
                    player.y = 450
                elif self.flow == "right":
                    player.x = 200
                    player.y = 450


class Room():
    def __init__(self, parent, top_door, right_door, bottom_door, left_door):
        self.x = 100
        self.y = 100
        self.width = 1000
        self.height = 700

        self.parent = parent

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.doors = []
        self.active_doors = [top_door, right_door, bottom_door, left_door]

        self.top_door = Door(self.x + 400, self.y, 200, 25, self, "top")
        self.bottom_door = Door(self.x + 400, self.y + self.height - 25, 200, 25, self, "bottom")
        self.left_door = Door(self.x, self.y + 250, 25, 200, self, "left")
        self.right_door = Door(self.x + self.width - 25, self.y + 250, 25, 200, self, "right")

        self.bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        if self.active_doors[0]:
            self.doors.append(self.top_door)
        if self.active_doors[1]:
            self.doors.append(self.right_door)
        if self.active_doors[2]:
            self.doors.append(self.bottom_door)
        if self.active_doors[3]:
            self.doors.append(self.left_door)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        self.enemy_group.draw(surface)
        self.bullet_group.draw(surface)

        for door in self.doors:
            door.draw(surface)

    def update(self, events, player):
        self.enemy_group.update(events, (player.x, player.y))
        self.bullet_group.update()

        for door in self.doors:
            door.update(events, player)

class Map():
    def __init__(self):
        self.rooms = []
        self.active_room = None

    def draw(self, surface):
        if self.active_room != None:
            self.active_room.draw(surface)

    def update(self, events, player):
        if self.active_room != None:
            self.active_room.update(events, player)

starting_map = Map()

room_1 = Room(starting_map, True, False, False, True)
room_2 = Room(starting_map, False, False, True, True)
room_3 = Room(starting_map, False, True, True, False)
room_4 = Room(starting_map, True, True, False, False)

room_1.top_door.target = room_2
room_2.bottom_door.target = room_1

room_2.left_door.target = room_3
room_3.right_door.target = room_2

room_3.bottom_door.target = room_4
room_4.top_door.target = room_3

room_4.right_door.target = room_1
room_1.left_door.target = room_4

starting_map.rooms.extend((room_1, room_2, room_3, room_4))

starting_map.active_room = starting_map.rooms[0]