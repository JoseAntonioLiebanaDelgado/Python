import pygame
import sys
import random

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('comarca.mp3')
pygame.mixer.music.play(-1)

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Atrapar los Anillos ;P")

background_image = pygame.image.load('Mordor.png')
background_image = pygame.transform.scale(background_image, (width, height))

white = (255, 255, 255)

gollum_image = pygame.image.load('gollum.png')
gollum_image = pygame.transform.scale(gollum_image, (100, 130))
gollum_rect = gollum_image.get_rect(midbottom=(width // 2, height))

ring_image = pygame.image.load('ring.png')
ring_image = pygame.transform.scale(ring_image, (30, 30))
ring_rect = ring_image.get_rect(topleft=(random.randint(0, width - 30), 0))

ring_speed = 20
gollum_speed = 0

score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gollum_rect.left > 0:
        gollum_speed = -25
    elif keys[pygame.K_RIGHT] and gollum_rect.right < width:
        gollum_speed = 25
    else:
        gollum_speed = 0
    gollum_rect.x += gollum_speed

    ring_rect.y += ring_speed
    if ring_rect.top > height:
        ring_rect.topleft = (random.randint(0, width - 30), -30)

    if gollum_rect.colliderect(ring_rect):
        score += 1
        ring_rect.topleft = (random.randint(0, width - 30), -30)

    screen.blit(background_image, (0, 0))

    screen.blit(gollum_image, gollum_rect)
    screen.blit(ring_image, ring_rect)

    score_text = font.render(f"Puntuación: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
