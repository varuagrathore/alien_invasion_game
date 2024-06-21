from alien import Alien

def create_fleet(ai_game):
    alien = Alien(ai_game)
    alien_width, alien_height = alien.rect.size
    available_space_x = ai_game.settings.screen_width - (alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)

    ship_height = ai_game.ship.rect.height
    available_space_y = (ai_game.settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = available_space_y // (2 * alien_height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_game, alien_number, row_number)

def create_alien(ai_game, alien_number, row_number):
    alien = Alien(ai_game)
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    ai_game.aliens.add(alien)
