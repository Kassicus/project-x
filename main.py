import pygame

import color
import player
import maps
import bullet
import enemy

pygame.init()

class Game():
    def __init__(self):
        self.width = 1200
        self.height = 900
        self.title = "Unnamed Roguelike"

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)

        self.running = True

        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.player = player.Player()

        self.map = maps.starting_map

    def start(self):
        enemy.spawn_enemies(5, self.map.active_room)

        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.black)

        self.map.draw(self.screen)

        self.player.draw(self.screen)

    def update(self):
        self.player.update(self.events)

        self.map.update(self.events, self.player)
    
        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()