import pygame
import pygame.locals


pygame.init()

screen = pygame.display.set_mode((500,150))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                print("pressed: LCTRL + BACKSPACE")

pygame.quit()
