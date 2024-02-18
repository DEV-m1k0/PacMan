import pygame
import Create_button
import sys
from DB import *
from constants import *
from run import GameController

class Start_menu(object):
    def __init__(self) -> None:
        db = DB(0)
        pygame.font.init()
        self.WIDTH = 800
        self.HEIGHT = 448
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.image.load("menu_back.jpg")
        self.font_text = pygame.font.Font("PressStart2P-Regular.ttf", 40)
        self.font_score = pygame.font.Font("PressStart2P-Regular.ttf", 20)
        self.text = self.font_text.render("PacMan", True, YELLOW)
        self.score = self.font_score.render(f"Your best score: {db.arr_score[0][0]}", True, WHITE)

    def start(self):
        self.run = True
        while self.run:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.text, (300, 25))
            self.screen.blit(self.score, (400, 425))

            self.start_button = Create_button.Button_start(self.screen, self.WIDTH/2-(128/2)+15, 300, 100, 100)
            self.start_button.check_hover(pygame.mouse.get_pos())
            self.check_events()
            
            if self.start_button.is_down:
                self.run = False

            pygame.display.update()
            
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
                sys.exit()

            self.start_button.check_down(event)

if __name__ == "__main__":
    start_menu = Start_menu()
    start_menu.start()

    game = GameController()
    game.startGame()
    while True:
        game.update()