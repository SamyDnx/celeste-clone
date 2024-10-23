import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.direction = 'R'
        self.width = 59
        self.height = 80
        self.image = pygame.image.load("assets/madeline.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 600
        self.top_mid = (self.rect.x + (self.width // 2), self.rect.y)
        self.bottom_mid = (self.top_mid[0], self.rect.y + self.height)
        self.left_mid = (self.rect.x, self.rect.y + (self.height // 2))
        self.right_mid = (self.rect.x + self.width, self.left_mid[1])

    def update_direction(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def update_collisions_points(self):
        self.top_mid = (self.rect.x + (self.width // 2), self.rect.y)
        self.bottom_mid = (self.top_mid[0], self.rect.y + self.height)
        self.left_mid = (self.rect.x, self.rect.y + (self.height // 2))
        self.right_mid = (self.rect.x + self.width, self.left_mid[1])

    def move_right(self):
        if self.direction == 'L':
            self.update_direction()
            self.direction = 'R'
        self.rect.x += self.velocity
        self.update_collisions_points()
    
    def move_left(self):
        if self.direction == 'R':
            self.update_direction()
            self.direction = 'L'
        self.rect.x -= self.velocity
        self.update_collisions_points()

    def move_down(self):
        self.rect.y += self.velocity
        self.update_collisions_points()

    def move_up(self):
        self.rect.y -= self.velocity
        self.update_collisions_points()
