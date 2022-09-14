import pygame
import sys
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from snake import *
from point import *

pygame.init()

screen_w, screen_h = 0, 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)

def start_game(window):
    screen_w, screen_h = window.get_width(), window.get_height()

    snake = Snake(window)
    point = Point(window)
    speed = 4

    game_over = False

    while not game_over:
        clock.tick(speed)
        window.fill((0, 200, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_DOWN or event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT):
                snake.set_direction(event.key)

        point.render_handler()
        snake_handler_result = snake.render_handler()

        text_surf = font.render(f"Score: {point.score}", True, (0, 0, 0))
        text_rect = text_surf.get_rect()

        window.blit(text_surf, text_rect)

        if snake.collide_point(point):
            snake.up_scale()
            point.init_point()

            if point.score % 10 == 0:
                speed += 1

        if snake.is_crashed() or snake_handler_result == IS_CRASHED:
            game_over = True

        pygame.display.flip()

    return point.score