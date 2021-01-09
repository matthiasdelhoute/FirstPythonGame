from Ship import Ship


class Player(Ship):
    killed = 0
    def __init__(self, pygame, os, x, y,health,bullets,vel):
        super().__init__(pygame, os, pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')),
                         180, bullets, x, y, health,vel
                         )





