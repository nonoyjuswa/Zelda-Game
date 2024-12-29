import pygame
import sys
from settings import *
from level import Level
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Game ni KIM')
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.menu = Menu(self.screen)
        self.show_menu = True

        main_sound = pygame.mixer.Sound('../audio/Sunny.ogg')
        main_sound.play(loops = -1)
        main_sound.set_volume(0.3)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.show_menu:
                    selection = self.menu.handle_input(event)
                    if selection == 0:  # Start Game
                        self.show_menu = False
                    elif selection == 1:  # Quit
                        pygame.quit()
                        sys.exit()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.level.toggle_menu()
                        elif event.key == pygame.K_ESCAPE:
                            self.show_menu = True

            if self.show_menu:
                self.menu.draw()
            else:
                self.screen.fill(WATER_COLOR)
                self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
