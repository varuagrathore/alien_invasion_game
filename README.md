```markdown
# Alien Invasion Game

## Overview

This is a Python implementation of the classic arcade game "Alien Invasion" using the Pygame library. The game involves a spaceship controlled by the player that must shoot down waves of incoming aliens.

## Directory Structure

```
alien_invasion/
│
├── alien_invasion.py
├── settings.py
├── ship.py
├── bullet.py
├── alien.py
├── stars.py
├── button.py
├── game_stats.py
├── utils.py  # Utility functions
├── game_functions/
│   ├── __init__.py
│   ├── event_handler.py
│   ├── bullet_handler.py
│   ├── alien_handler.py
│   ├── screen_updater.py
│   ├── fleet_handler.py
```

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/alien_invasion.git
   cd alien_invasion
   ```

2. **Install Pygame:**

   ```bash
   pip install pygame
   ```

### Running the Game

To start the game, run the `alien_invasion.py` file:

```bash
python alien_invasion.py
```

## Game Controls

- **Right Arrow Key:** Move the ship to the right
- **Left Arrow Key:** Move the ship to the left
- **Spacebar:** Shoot bullets
- **Q Key:** Quit the game

## Project Structure

- **alien_invasion.py:** The main game file that initializes the game and starts the game loop.
- **settings.py:** Contains all the game settings such as screen dimensions, ship speed, bullet speed, etc.
- **ship.py:** Defines the Ship class, which manages the player's spaceship.
- **bullet.py:** Defines the Bullet class, which manages the bullets fired by the ship.
- **alien.py:** Defines the Alien class, which manages the alien invaders.
- **stars.py:** Defines the Stars class, which creates a starry background.
- **button.py:** Defines the Button class, which manages the play button.
- **game_stats.py:** Defines the GameStats class, which tracks the game's statistics.
- **utils.py:** Contains utility functions used across different modules.
- **game_functions/:** A directory containing various game logic modules:
  - **event_handler.py:** Handles all the user input events.
  - **bullet_handler.py:** Manages the behavior of bullets.
  - **alien_handler.py:** Manages the behavior of aliens.
  - **screen_updater.py:** Handles updating the game screen.
  - **fleet_handler.py:** Manages the creation and behavior of the alien fleet.



## Acknowledgments

- The game is inspired by the classic arcade game "Space Invaders".
- Thanks to the Pygame community for their tutorials and resources.
```


