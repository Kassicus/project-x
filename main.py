import pygame

import color
import player

pygame.init()

class Game():
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 900
        self.TITLE = "Unnamed Roguelike"

        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption(self.TITLE)

        self.running = True

        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.player = player.Player()

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.BLACK)

        self.player.draw(self.screen)

    def update(self):
        self.player.update(self.events)
    
        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()