import pygame,sys
import sys
import os

pygame.init()

clock = pygame.time.Clock()        #Controlling the speed of updates
screen = pygame.display.set_mode((900,75))  #Size input screen

pygame.display.set_caption('text input')      #Name input screen

#User text, input field, background, background color, input field color

userText = ' '
font = pygame.font.SysFont('Arial',32) 
input_rect = pygame.Rect(10,15,500,40)
active = False
colorAktiv = pygame.Color('green')
colorDontAktiv = pygame.Color('red')
color = colorDontAktiv
active = False

while True:    
    
   for event in pygame.event.get():   #Checking for program exit events
      if event.type==pygame.QUIT:
         pygame.quit()
         sys.exit()
              
      if event.type==pygame.MOUSEBUTTONDOWN:         #Activate a field by clicking
         if input_rect.collidepoint(event.pos):
            active = True

      if event.type == pygame.KEYDOWN:       #If button press
         if active == True:
         
            if event.key == pygame.K_BACKSPACE:     #If K_BACKSPACE press - erase last character
               userText = userText[:-1]
               
            elif event.key == pygame.K_RETURN:      #If K_RETURN press - create folder/file
               print("User input:", userText)
               
               try:
                  folder, filename = userText.split('/')
                  os.makedirs(folder, exist_ok=True)
                  
                  with open(userText, 'w') as file:
                     file.write("Your initial content here.")
                     print(f"Folder '{folder}' and file '{filename}' created successfully.")
                     
               except ValueError:
                  print("Invalid input format. Please use 'folder/filename'.")
                  
               except Exception as e:
                  print(f"An error occurred: {e}")
                  
            else:
               userText+=event.unicode              #Add char in string
          
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
