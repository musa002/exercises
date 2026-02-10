import pygame
import sys

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

ball = pygame.image.load("ball.png")

x, y = 100, 100

vx, vy = 3, 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    x += vx
    y += vy

  
    if x <= 0 or x + ball.get_width() >= 640:
        vx = -vx
    if y <= 0 or y + ball.get_height() >= 480:
        vy = -vy
        
    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    clock.tick(60)
