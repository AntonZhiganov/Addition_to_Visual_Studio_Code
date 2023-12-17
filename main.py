import pygame
import pygame.locals
import subprocess

pygame.init()

def runCreate():                                               
    subprocess.run(["python", "/home/anton/Addition_to_Visual_Studio_Code/createFoldersandFile.py"])    #Executes the program whose path is in parentheses

screen = pygame.display.set_mode((500,150))     #First screen
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F2 and pygame.key.get_mods() & pygame.KMOD_SHIFT:  #If the key combination is correct, 
                print("pressed: Shift + F2")                                       #it displays (pressed: Shift + F2) and 
                runCreate()                                                        #launches the folder creation program
                
pygame.quit()