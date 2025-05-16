import sys
import pygame
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings, screen, ship):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
# Отображение последнего прорисованного экрана.
        pygame.display.flip()
def check_events(ship):
     #Обрабатывает нажатия клавиш и события мыши
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False