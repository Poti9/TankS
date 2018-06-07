
import pygame
import state

import config
from gamestate import GameState
from player import Player
RED = (255, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 100)
LIGHTBLUE = (0, 0, 255)

class TitleState:

    def __init__(self):
        pass

    def process_input(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state.state = GameState()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLUE)
        myfont = pygame.font.SysFont("Arial", 50)
        label = myfont.render("PRESS SPACE TO START", 1, GREEN)
        screen.blit(label,(100,100))