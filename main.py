import pygame,sys

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900,75))  #Size input screen

pygame.display.set_caption('text input')      #Name input screen

userText = ' '
font = pygame.font.SysFont('frenchscript',32) 
input_rect = pygame.Rect(10,15,500,40)
active = False
colorAktiv = pygame.Color('green')
colorDontAktiv = pygame.Color('red')
color = colorDontAktiv
active = False

while True:    
    
   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         pygame.quit()
         sys.exit()
              
      if event.type==pygame.MOUSEBUTTONDOWN:
         if input_rect.collidepoint(event.pos):
            active = True

      if event.type == pygame.KEYDOWN:
         if active == True:
         
            if event.key == pygame.K_BACKSPACE:
               userText = userText[:-1]
            else:
               userText+=event.unicode
          
   screen.fill('black')
   if active:
      color=colorAktiv
   else:
      color=colorDontAktiv
      
   pygame.draw.rect(screen,color,input_rect,2)
     
      
   text_surface = font.render(userText,True,(255,255,255))
   screen.blit(text_surface,(input_rect.x + 5, input_rect.y +5))
   input_rect.w=max(100,text_surface.get_width() + 10)
   pygame.display.flip()
   clock.tick(60)
