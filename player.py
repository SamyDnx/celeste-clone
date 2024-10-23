import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.direction = 'R'
        self.image = pygame.image.load("assets/madeline.png")
        self.image = pygame.transform.scale(self.image, (59, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 645

    def update_direction(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def move_right(self):
        if self.direction == 'L':
            self.update_direction()
            self.direction = 'R'
        self.rect.x += self.velocity
    
    def move_left(self):
        if self.direction == 'R':
            self.update_direction()
            self.direction = 'L'
        self.rect.x -= self.velocity

