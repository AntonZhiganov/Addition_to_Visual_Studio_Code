import pygame
import pygame.locals


pygame.init()

screen = pygame.display.set_mode((500,150))

running = True

user_text = ''
font = pygame.font.SysFont('frenchscript',32) 
input_rect = pygame.Rect(200,200,140,40)
active=False
color_ac=pygame.Color('green')
color_pc=pygame.Color('red')
color=color_pc
active=False

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            running = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                
                running = False
                
            elif event.key == pygame.K_BACKSPACE:
                
                user_text = user_text[:-1]
                
            elif event.key == pygame.K_F2 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                active = True
                print("pressed: Shift + F2")

pygame.quit()
