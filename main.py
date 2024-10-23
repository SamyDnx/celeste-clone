import pygame
from player import Player
from game import Game

pygame.init()

WIDTH, HEIGHT = 1600, 900
CELL_SIZE = 10


FPS = 60
clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deleste")

background = pygame.image.load("assets/1a-01.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

game = Game()

run = True
while run:

    window.blit(background, (0, 0))
    window.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_ESCAPE):
        run = False
    elif game.pressed.get(pygame.K_d) and game.player.rect.x < 1535:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 35:
        game.player.move_left()
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    clock.tick(FPS)

pygame.quit()
quit()
