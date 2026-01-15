import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.JPG")

window.fill((0,0,0))
window.blit(robot, (0, 0))
window.blit(robot, (400, 0))
window.blit(robot, (0, 300))
window.blit(robot, (400, 300))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()