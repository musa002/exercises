import pygame
import sys

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.jpg")

x = 0
y = 0
speed = 2
clock = pygame.time.Clock()

direction = "right"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if direction == "right":
        x += speed
        if x + robot.get_width() >= 640:
            x = 640 - robot.get_width()
            direction = "down"

    elif direction == "down":
        y += speed
        if y + robot.get_height() >= 480:
            y = 480 - robot.get_height()
            direction = "left"

    elif direction == "left":
        x -= speed
        if x <= 0:
            x = 0
            direction = "up"

    elif direction == "up":
        y -= speed
        if y <= 0:
            y = 0
            direction = "right"

    clock.tick(60)
