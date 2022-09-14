import pygame
from game import *

screen_w, screen_h = 600, 600

best_score, last_score = 0, 0

pygame.init()
window = pygame.display.set_mode([screen_w, screen_h])
pygame.display.set_caption("Snake Game")

is_running = True
while is_running:
    window.fill((0, 200, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        elif event.type == KEYDOWN and event.key ==  pygame.K_RETURN:
            current_score = start_game(window)
            last_score = current_score
            best_score = max(best_score, current_score)

    text_surf = font.render(f"Last score: {last_score}", True, (0, 0, 0))
    text_rect = text_surf.get_rect()
    window.blit(text_surf, text_rect)

    text_surf = font.render(f"Best score: {best_score}", True, (0, 0, 0))
    text_rect = text_surf.get_rect(x = screen_w - 250)
    window.blit(text_surf, text_rect)

    text_surf = font.render("Press ENTER to start!", True, (0, 0, 0))
    text_rect = text_surf.get_rect(x = (screen_w - 300) / 2, y = (screen_h - 50) / 2)
    window.blit(text_surf, text_rect)

    pygame.display.flip()
    

pygame.quit()