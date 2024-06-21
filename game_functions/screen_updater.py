import pygame

def update_screen(ai_game):
    ai_game.screen.fill(ai_game.settings.bg_color)
    ai_game.stars.draw_stars()
    ai_game.ship.blitme()
    for bullet in ai_game.bullets.sprites():
        bullet.draw_bullet()
    ai_game.aliens.draw(ai_game.screen)
    ai_game.sb.show_score()
    if not ai_game.stats.game_active:
        ai_game.play_button.draw_button()
    pygame.display.flip()
