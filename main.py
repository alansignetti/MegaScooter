
# Importamos todos los modulos de pygame
import pygame,sys
from pygame.locals import *

# Inicializamos todos los modulos de pygame
pygame.init()

# Variable para las ventanas 
ANCHO = 1280
LARGO = 720

ventana = pygame.display.set_mode((ANCHO, LARGO))

#Colocar el titulo a la ventana
pygame.display.set_caption("MegaScooter")

#Declaramos las funciones

def cargar_piso (piso1):
    ventana.blit(piso1,(0,600))
    ventana.blit(piso1,(1000,600)) 

    

# Bucle principal
while True:

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    # Cargar la imagen en una variable.
    piso1 = pygame.image.load("Imagenes/piso1.jpg") 
    moto_con_personaje = pygame.image.load("Imagenes/Personaje_con_moto.png")

    #Cargamos el piso en la ventana, con funciones.
    cargar_piso (piso1)

    #Cargamos las imagenes del personaje
    ventana.blit(moto_con_personaje,(0,500))
    

    #Actualiza la ventana
    pygame.display.update()



    