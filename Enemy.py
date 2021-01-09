from Ship import Ship
import random


class Enemy(Ship):
    def __init__(self, pygame, os, x, y, health, bullets, vel):
        super().__init__(pygame, os, pygame.image.load(os.path.join('Assets', 'spaceship_red.png')),
                         0, bullets, x, y, health, vel
                         )

    def handle_movement(self, pygame, max_left, max_right, max_up, max_below):
        movement = random.randint(0, 3)
        if movement == 0 and self.rect.x - self.vel > max_left:  # LEFT
            self.rect.x -= self.vel
        if movement == 1 and self.rect.x + self.vel + self.width < max_right:  # RIGHT
            self.rect.x += self.vel
        if movement == 2 and self.rect.y - self.vel > max_up:  # UP
            self.rect.y -= self.vel
        if movement == 3 and self.rect.y + self.vel + self.height < max_below:  # DOWN
            self.rect.y += self.vel

    def handle_fire(self,pygame):
        if random.randint(0,70) ==55 and len(self.bullets) < self.max_bullets:
            bullet = pygame.Rect(self.rect.x + self.width // 2, self.rect.y, 5,20)
            self.add_bullet(bullet)
            self.bullet_fire_sound.play()