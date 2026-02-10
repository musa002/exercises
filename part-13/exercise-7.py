import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            if event.key == pygame.K_RIGHT:
                print("right")

        if event.type == pygame.QUIT:
            exit()