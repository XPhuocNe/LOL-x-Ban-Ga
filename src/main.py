import pygame
import sys

class Game:
    """Main game class that handles initialization, game loop and cleanup."""

    def __init__(self):
        """Initialize Pygame and game window."""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GAME LOL x BẮN GÀ")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        """Handle user input and quit event."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Update game logic (to be implemented)."""
        pass

    def draw(self):
        """Draw everything on screen (to be implemented)."""
        self.screen.fill((0, 0, 0))  # Black background

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
