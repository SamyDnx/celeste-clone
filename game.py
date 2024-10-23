import pygame
from player import Player

WIDTH, HEIGHT = 1600, 900

RED = pygame.Color(255, 0, 0)       # Enemies
GREEN = pygame.Color(0, 255, 0)     # Finish
BLUE = pygame.Color(0, 0, 255)      # Walls

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

    def check_collisions(self, player):
        if self.collisions[player.bottom_mid] == BLUE or self.collisions[player.right_mid] == BLUE or self.collisions[player.left_mid] == BLUE or self.collisions[player.top_mid] == BLUE:
            return "walls"

        elif self.collisions[player.bottom_mid] == RED or self.collisions[player.right_mid] == RED or self.collisions[player.left_mid] == RED or self.collisions[player.top_mid] == RED:
            return "enemies"
        
        elif self.collisions[player.bottom_mid] == GREEN or self.collisions[player.right_mid] == GREEN or self.collisions[player.left_mid] == GREEN or self.collisions[player.top_mid] == GREEN:
            return "finish"
