import pygame,sys
import sys
import os
from ewmh import EWMH        #To get active windows

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

def activeVS():                          #If VS active, it executes the code further
   ewmh = EWMH()
   windows = ewmh.getClientList()        #gets a list of windows
   window_titles = [ewmh.getWmName(window).decode('utf-8') if ewmh.getWmName(window) else "" for window in windows]
   
   print(window_titles)
   
   for title in window_titles:            #If Visual Studio is in the list of windows, it continues execution
        if "Visual Studio" in title:  
            return True
   return False                           #If Visual Studio is not in the list of windows, 
                                          #it displays an error and closes the program

def createFoldresAndFile(path):                #Function to create many folders
   components = path.split('/')
   current_path = ''
    
   for i, component in enumerate(components[:-1]):           #Creating folders and a file, this part 
      current_path = os.path.join(current_path, component)   #of the code adds all the names that the 
      os.makedirs(current_path, exist_ok=True)               #user wrote and understands that these are folders (Excluding the very last one which will be a file)
    
   filename = components[-1]                                 #This code selects the last component from the list of path components and adds it to the current path.
   current_path = os.path.join(current_path, filename)
   with open(current_path, 'w') as file:
      file.write("File create")
           
   print(f"Folder(s) and file '{filename}' created successfully.")      #Show "Folder(s) and file ..."

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
               
               if activeVS():                        #If VS active, it creates a folder
                     createFoldresAndFile(userText)
               else:
                     print("Visual Studio is not open. Exiting program.")
                     pygame.time.delay(5000)
                     pygame.quit()
                     sys.exit()
                  
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
   clock.tick(60)           #60FPS