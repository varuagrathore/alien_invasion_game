from game_functions import fleet_handler
import pygame

def update_bullets(ai_game):
    ai_game.bullets.update()
    for bullet in ai_game.bullets.copy():
        if bullet.rect.bottom <= 0:
            ai_game.bullets.remove(bullet)
    check_bullet_alien_collisions(ai_game)

def check_bullet_alien_collisions(ai_game):
    collisions = pygame.sprite.groupcollide(ai_game.bullets, ai_game.aliens, False, True)
    if collisions:
        for aliens in collisions.values(): 
            ai_game.stats.score += ai_game.settings.alien_points *len(aliens)
        ai_game.sb.prep_score()
        ai_game.sb.check_high_score()
    if not ai_game.aliens:
        ai_game.bullets.empty()
        ai_game.settings.increase_speed()
        ai_game.stats.level +=1
        ai_game.sb.prep_level()
        fleet_handler.create_fleet(ai_game)
