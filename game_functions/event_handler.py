import sys
import pygame
from bullet import Bullet
from game_functions import fleet_handler

def check_events(ai_game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_game)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_game)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            check_play_button(ai_game, mouse_pos)

def check_keydown_events(event, ai_game):
    if event.key == pygame.K_RIGHT:
        ai_game.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ai_game.ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_game)

def check_keyup_events(event, ai_game):
    if event.key == pygame.K_RIGHT:
        ai_game.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ai_game.ship.moving_left = False

def fire_bullet(ai_game):
    if len(ai_game.bullets) < ai_game.settings.bullets_allowed:
        new_bullet = Bullet(ai_game)
        ai_game.bullets.add(new_bullet)

def check_play_button(ai_game, mouse_pos):
    button_clicked = ai_game.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not ai_game.stats.game_active:
        ai_game.settings.initialize_dynamic_settings()
        ai_game.stats.reset_stats()
        ai_game.stats.game_active = True
        ai_game.sb.prep_score()
        ai_game.sb.prep_level()
        ai_game.sb.prep_ships()

        ai_game.aliens.empty()
        ai_game.bullets.empty()

        fleet_handler.create_fleet(ai_game)
        ai_game.ship.center_ship()

        pygame.mouse.set_visible(False)
