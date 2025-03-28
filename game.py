import pygame
import sys
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Choppy Orc")
        self.clock = pygame.time.Clock()
        self.running = True

        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        
        # Create player
        self.player = Player(400, 300)
        self.all_sprites.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        self.player.handle_input()
        self.all_sprites.update()

    def render(self):
        self.screen.fill((0, 0, 0))  # Black background
        
        # Draw all sprites
        self.all_sprites.draw(self.screen)
        
        pygame.display.flip()

    def run(self):
        while self.running:
            self.process_events()
            self.update()
            self.render()
            self.clock.tick(60)  # 60 FPS

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run() 