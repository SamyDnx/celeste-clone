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
game.get_all_collisions()

run = True
while run:

    window.blit(background, (0, 0))
    window.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_ESCAPE):
        run = False

    elif game.pressed.get(pygame.K_d):
        if game.check_right_collisions() == "walls":
            game.player.rect.x -= game.player.velocity
            game.player.update_collisions_points()
        game.player.move_right()

    elif game.pressed.get(pygame.K_q):
        if game.check_left_collisions() == "walls":
            game.player.rect.x += game.player.velocity
            game.player.update_collisions_points()
        game.player.move_left()

    elif game.pressed.get(pygame.K_s):
        if game.check_bottom_collisions() == "walls":
            game.player.rect.y -= game.player.velocity
            game.player.update_collisions_points()
        game.player.move_down()

    elif game.pressed.get(pygame.K_z):
        if game.check_top_collisions() == "walls":
            game.player.rect.y += game.player.velocity
            game.player.update_collisions_points()
        game.player.move_up()
    
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
