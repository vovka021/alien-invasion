import sys
import pygame
from pygame.sprite import Group 
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
def run_game():
# Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
     # Создание групп
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)    
    #Запуск осн цикла игры
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Удаление пуль, вышедших за край экрана.
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()      