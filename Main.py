import pygame
import os
import Player
import Enemy

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60

BORDER = pygame.Rect(0, HEIGHT - HEIGHT // 5, WIDTH, 10)

PLAYER_HIT = pygame.USEREVENT + 1
ENEMY_HIT = pygame.USEREVENT + 2

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def draw_window(player, enemies):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    player_health_text = HEALTH_FONT.render("Health: " + str(player.health), 1, WHITE)
    WIN.blit(player_health_text, (10, 10))

    WIN.blit(player.spaceship, (player.rect.x, player.rect.y))

    for enemy in enemies:
        WIN.blit(enemy.spaceship, (enemy.rect.x, enemy.rect.y))
        for bullet in enemy.bullets:
            pygame.draw.rect(WIN, RED, bullet)

    for bullet in player.bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)


def handle_bullets(enemy, player):
    for bullet in player.bullets:
        bullet.y -= player.bullet_vel
        if enemy.rect.colliderect(bullet):
            enemy.health -= 1
            enemy.bullet_hit_sound.play()
            player.killed +=1
            player.remove_bullet(bullet)
        elif bullet.y < 0:
            player.remove_bullet(bullet)

    for bullet in enemy.bullets:
        bullet.y += enemy.bullet_vel
        if player.rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            enemy.bullets.remove(bullet)
        elif bullet.y > HEIGHT:
            enemy.bullets.remove(bullet)


def create_enemy(enemies, width, height):
    enemy = Enemy.Enemy(pygame, os, width, height, 10, 5,5)
    enemies.append(enemy)


def main():
    player = Player.Player(pygame, os, WIDTH // 2, HEIGHT - HEIGHT // 7, 10,  30,3)
    enemies = []
    create_enemy(enemies, WIDTH - (WIDTH // 3) * 2, HEIGHT // 8)
    create_enemy(enemies, WIDTH - WIDTH // 3, HEIGHT // 8)

    winner_text = ""

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(player.bullets) < player.max_bullets:
                    bullet = pygame.Rect(player.rect.x + player.width // 2, player.rect.y, 10, 5)
                    player.add_bullet(bullet)
                    player.bullet_fire_sound.play()
            if event.type == PLAYER_HIT:  # PLAYER HIT
                player.health -= 1
                player.bullet_hit_sound.play()
        for enemy in enemies:
            if enemy.health == 0:
                enemies.remove(enemy)

        if len(enemies) == 0:
            winner_text = "You killed all enemies! You've killed "+str(player.killed)
        if player.health == 0:
            winner_text = "You lost! You've killed "+str(player.killed)
        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()

        player.handle_movement(pygame, keys_pressed, 0, WIDTH, BORDER.y + 15, HEIGHT, pygame.K_LEFT, pygame.K_RIGHT,
                               pygame.K_UP,
                               pygame.K_DOWN)

        for enemy in enemies:
            enemy.handle_fire(pygame)
            enemy.handle_movement(pygame, 0, WIDTH, 0, BORDER.y - 15)
            handle_bullets(enemy, player)

        draw_window(player, enemies)

    main()


if __name__ == '__main__':
    main()
