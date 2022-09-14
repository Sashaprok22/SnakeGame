import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

IS_GOOD = 0
IS_CRASHED = 1

class Snake():
    size = 20
    move_x = 0
    move_y = -size
    snake_size = 1

    def __init__(self, window):
        self.window = window
        self.snake = []
        self.pos = {"x":0, "y":0}

    def render_handler(self):
        final_status = IS_GOOD

        self.pos["x"] += self.move_x
        self.pos["y"] -= self.move_y

        block = pygame.Rect(self.pos["x"], self.pos["y"], self.size, self.size)
        self.snake.append(block)

        if len(self.snake) > self.snake_size:
            del self.snake[0]

        for i, rect in enumerate(self.snake):
            pygame.draw.rect(self.window, (255, 255, 255), rect)
            
            if rect.collidelist(self.snake) != i:
                final_status = IS_CRASHED
                pass

        return final_status

    def is_crashed(self):
        screen_w, screen_h = self.window.get_width(), self.window.get_height()
        return self.pos["x"] < 0 or self.pos["x"] > screen_w - self.size or self.pos["y"] < 0 or self.pos["y"] > screen_h - self.size

    def up_scale(self):
        self.snake_size += 1

    def set_direction(self, key):
        self.move_x = 0
        self. move_y = 0
        if key == K_UP:
            self.move_y = self.size
        elif key == K_DOWN:
            self.move_y = -self.size
        elif key == K_LEFT:
            self.move_x = -self.size
        elif key == K_RIGHT:
            self.move_x = self.size

    def collide_point(self, point):
        return self.snake[-1].collidepoint(point.point)

        