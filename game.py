import pygame
from player import Player

WIDTH, HEIGHT = 1600, 900

RED = pygame.Color(254, 0, 0, 255)       # Enemies
GREEN = pygame.Color(0, 254, 0, 255)     # Finish
BLUE = pygame.Color(0, 0, 254, 255)      # Walls

class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {}
        self.level_image = pygame.image.load("assets/1a-01_col.jpg")
        self.level_image = pygame.transform.scale(self.level_image, (WIDTH, HEIGHT))
        self.collisions = {}

    def get_all_collisions(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                px = self.level_image.get_at((x, y))
                self.collisions[(x, y)] = px

    def check_right_collisions(self):
        if self.collisions[self.player.right_mid] == BLUE:
            return "walls"
        elif self.collisions[self.player.right_mid] == RED:
            return "enemies"
        elif self.collisions[self.player.right_mid] == GREEN:
            return "finish"
    
    def check_left_collisions(self):
        if self.collisions[self.player.left_mid] == BLUE:
            return "walls"
        elif self.collisions[self.player.left_mid] == RED:
            return "enemies"
        elif self.collisions[self.player.left_mid] == GREEN:
            return "finish"

    def check_top_collisions(self):
        if self.collisions[self.player.top_mid] == BLUE:
            return "walls"
        elif self.collisions[self.player.top_mid] == RED:
            return "enemies"
        elif self.collisions[self.player.top_mid] == GREEN:
            return "finish"

    def check_bottom_collisions(self):
        if self.collisions[self.player.bottom_mid] == BLUE:
            return "walls"
        elif self.collisions[self.player.bottom_mid] == RED:
            return "enemies"
        elif self.collisions[self.player.bottom_mid] == GREEN:
            return "finish"
