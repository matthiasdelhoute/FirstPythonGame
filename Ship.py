class Ship:
    def __init__(self, pygame, os, image, rotation, max_bullets, x, y, health,vel):
        self.image = image
        self.rotation = rotation
        self.max_bullets = max_bullets
        self.vel = vel
        self.bullet_vel = 2
        self.width = 55
        self.height = 40
        self.size = (self.width, self.height)
        self.bullets = []
        self.bullet_hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
        self.bullet_fire_sound = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
        self.spaceship = pygame.transform.rotate(pygame.transform.scale(self.image, self.size), self.rotation)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.health = health

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def handle_movement(self, pygame, keys_pressed, max_left, max_right, max_up, max_below,key_left,key_right,key_up,key_down):
        if keys_pressed[key_left] and self.rect.x - self.vel > max_left:  # LEFT
            self.rect.x -= self.vel
        if keys_pressed[key_right] and self.rect.x + self.vel + self.width < max_right:  # RIGHT
            self.rect.x += self.vel
        if keys_pressed[key_up] and self.rect.y - self.vel > max_up:  # UP
            self.rect.y -= self.vel
        if keys_pressed[key_down] and self.rect.y + self.vel + self.height < max_below:  # DOWN
            self.rect.y += self.vel
