import pygame
import color
import maps
import player

pygame.init()

class Game():
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 900
        self.TITLE = "Untitled Roguelike"

        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption(self.TITLE)

        self.running = True
        self.clock = pygame.time.Clock()

        self.events = pygame.event.get()

        self.testMap = maps.Map()

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

        self.testMap.draw(self.screen)

        self.player.draw(self.screen)

    def update(self):
        self.testMap.update(self.events)

        self.player.update(self.events)

        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()