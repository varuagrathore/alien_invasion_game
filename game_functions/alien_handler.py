import pygame
from time import sleep
from game_functions import fleet_handler

def update_aliens(ai_game):
    check_fleet_edges(ai_game)
    ai_game.aliens.update()
    if pygame.sprite.spritecollideany(ai_game.ship, ai_game.aliens):
        ship_hit(ai_game)
    check_aliens_bottom(ai_game)

def check_fleet_edges(ai_game):
    for alien in ai_game.aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_game)
            break

def change_fleet_direction(ai_game):
    for alien in ai_game.aliens.sprites():
        alien.rect.y += ai_game.settings.fleet_drop_speed
    ai_game.settings.fleet_direction *= -1

def check_aliens_bottom(ai_game):
    screen_rect = ai_game.screen.get_rect()
    for alien in ai_game.aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_game)
            break

def ship_hit(ai_game):
    if ai_game.stats.ship_left > 0:
        ai_game.stats.ship_left -= 1
        ai_game.sb.prep_ships()
        ai_game.aliens.empty()
        ai_game.bullets.empty()

        fleet_handler.create_fleet(ai_game)
        ai_game.ship.center_ship()

        sleep(0.5)
    else:
        ai_game.stats.game_active = False
        pygame.mouse.set_visible(True)
