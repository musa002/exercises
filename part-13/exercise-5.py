import pygame
import sys
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot = pygame.image.load("robot.jpg")

center_x, center_y = 320, 240 
radius = 150                  
num_robots = 10               
speed = 0.02  

angles = [2 * math.pi * i / num_robots for i in range(num_robots)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))

    for i in range(num_robots):
        angles[i] += speed 
        x = center_x + radius * math.cos(angles[i]) - robot.get_width() // 2
        y = center_y + radius * math.sin(angles[i]) - robot.get_height() // 2
        window.blit(robot, (x, y))

    pygame.display.flip()
    clock.tick(60)
