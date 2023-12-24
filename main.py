import pygame,sys
import sys
import os
from ewmh import EWMH        #To get active windows
import psutil     #Import to access system information

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

def activeVS():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):   #obtaining information about running processes in the system (identifier, name, command line)
        if "code" in process.info['name'].lower() and any("vscode" in arg.lower() for arg in process.info['cmdline']): #Checks whether there is (Code and vs code) in the process name
            projectPath = process.info['cmdline'][-1].strip()   #Gets the path to the active project from the last command line argument of the process
            print(f"Active project in Visual Studio Code: {projectPath}") #Active project
            return projectPath

    return None




def createFoldresAndFile(path):
    vs_project_path = activeVS()         #Getting the path of the active project in Visual Studio Code
    if vs_project_path:
        targetDir = os.path.join(path) #Create the full path to the target directory

        components = targetDir.split('/')  #Separating folders and files
        current_path = ''

         # Iterate through the components, creating folders but the last one is a file
        for i, component in enumerate(components[:-1]):
            current_path = os.path.join(current_path, component)
            os.makedirs(current_path, exist_ok=True)

        filename = components[-1] # Get the filename from the last component
        
        current_path = os.path.join(current_path, filename) # Create the full path to the file
        with open(current_path, 'w') as file:
            file.write("File create")

        print(f"Folder(s) and file '{filename}' created successfully in the your folder")
    else:
        print("Visual Studio Code is not open or there is no active project.")

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