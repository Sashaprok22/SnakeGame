import pygame, snake
from random import randint

class Point():
    score = -1
    size = snake.Snake.size * 0.5
    normal_size = snake.Snake.size * 0.5

    def __init__(self, window):
        self.window = window
        self.init_point()

    def init_point(self):
        self.score += 1
        screen_w, screen_h = self.window.get_width(), self.window.get_height()
        x, y = randint(0, (screen_w - self.normal_size) * 0.1) * 10, randint(0, (screen_h - self.normal_size) * 0.1) * 10
        self.point = [x + self.normal_size * 0.5, y + self.normal_size * 0.5]

    def render_handler(self):
        self.size = self.size * 0.75 if self.size == self.normal_size else self.size / 0.75
        pygame.draw.circle(self.window, (200, 0, 0), self.point, self.size)