# Importamos todos los modulos de pygame
import pygame,sys
from pygame.locals import *

import random # para los numeros aleatorios

# Inicializamos todos los modulos de pygame
pygame.init()

# Variable para las ventanas 
ANCHO = 1280
LARGO = 720
Blanco = pygame.Color(255, 255, 255)


ventana = pygame.display.set_mode((ANCHO, LARGO))
fuente_Puntuacion=pygame.font.Font("fuentes/8-BIT WONDER.TTF",25)




#Colocar el titulo a la ventana
pygame.display.set_caption("MegaScooter")



# En esta clase vamos a guardar las variables que utilizamos para hacer el fondo y el piso movil.
class Variables_CargaImagenes():

    def __init__(self):
         self.xPiso=0       
         self.xFondo=0
         self.numeroVelocidad=15
         self.puntos=0
         self.xobstaculo = 1280
         self.yobstaculo = 540
         self.resta=15



      #Videos para hacer el fondo y el piso movil https://www.youtube.com/watch?v=Ftln3VrFV6s&list=PLVzwufPir356RMxSsOccc38jmxfxqfBdp&index=4   

def cargar_fondo():
    #-----------------------------Fondo----------------------------------------------
    fondo= pygame.image.load("Imagenes/fondo22.jpg").convert()
    x_rel_Fondo= variables.xFondo % fondo.get_rect().width  # Hacemos el valor de "x" dividido "%" el ancho del fondo "fondo.get_rect().width"
    ventana.blit(fondo, (x_rel_Fondo - fondo.get_rect().width, 0))

    # Este if permite que el fondo se repita indefinidamente
    if(x_rel_Fondo<ANCHO):
        ventana.blit(fondo,(x_rel_Fondo,0))
    variables.xFondo-=8  #Cambias la velocidad del fondo.
    #----------------------------Fin Fondo-------------------------------------------



def cargar_piso ():
    #-------------------------------Piso-------------------------------------------
    altoPiso = 597 #Calculamos el alto del piso
    
    if velocidad_a == True:
        variables.numeroVelocidad += 0.05/5
        
    piso = pygame.image.load("Imagenes/piso22.jpg").convert()   #cargamos la imagen en variable piso
    
    x_rel_Piso= variables.xPiso % piso.get_rect().width  #despues del % el comando obtiene el ancho
    #de la foto siendo el divisor de xPiso devuelve el resto

    ventana.blit(piso, (x_rel_Piso-piso.get_rect().width, altoPiso))
    if(x_rel_Piso<ANCHO):
        ventana.blit(piso,(x_rel_Piso,altoPiso)) #Mostramos la imagen
        variables.xPiso-=variables.numeroVelocidad #Calcula la velocidad mientras el numero sea mas alto mas rapido ira el movimiento de la imagen
    
        # xPiso es la cantidad de pixeles por segundo

    #-----------------------------FinPiso-------------------------------------------



def obstaculo ():

    global iteradorObstaculo

    if cambiarObstaculo==1:
        
        vobstaculo=[pygame.image.load('Imagenes/Sierras1.png'),
                    pygame.image.load('Imagenes/Sierras2.png'),
                    pygame.image.load('Imagenes/Sierras3.png'),
                    pygame.image.load('Imagenes/Sierras4.png')
                    ] 

        if iteradorObstaculo + 1 >= 4: #Este iterador recorre las 4 imagenes de la sierra
            iteradorObstaculo = 0 
          
        variables.xobstaculo = variables.xobstaculo - variables.resta  
        ventana.blit(vobstaculo[iteradorObstaculo // 1], (int(variables.xobstaculo), int(variables.yobstaculo)))
        iteradorObstaculo += 1

        if variables.xobstaculo <= -200 : 
            variables.xobstaculo = 1280
            variables.resta +=0.5


    else:
        vobstaculo= pygame.image.load("Imagenes/Pincho.png") #Agregamos la imagen del obstaculo

        if variables.xobstaculo >= -100:    #Un if desplaza el obstaculo hacia la izquierda y cuando llega al final, lo devuelve al principio.
         
            variables.xobstaculo = variables.xobstaculo - variables.resta
            ventana.blit (vobstaculo,(variables.xobstaculo,variables.yobstaculo)) 

        else:
            variables.xobstaculo = 1280 #Cuando el obstaculo llegue a la punta izquierda, setea la variable para ponerlo al principio. 
            variables.resta +=0.5  #En cuanto queres que se incremente cada vez que vuelva a aparecer de vuelta el obstaculo




def puntuacion():
    texto_de_puntos=fuente_Puntuacion.render("Puntos "+str(variables.puntos),True,Blanco)
    ventana.blit(texto_de_puntos,(900,15))

def movimiento_moto ():

    #-----------------------------Logica para mover la moto-------------------------------
    #Variables globales
    global cuentaPasos
    global x

    #Estos if anidados definen segun la tecla que se aprete las imagenes que se tiene que mostrar

    #Contador de pasos
    if cuentaPasos + 1 >= 4:   #>= 4 porque las fotos del movimiento de la moto son 4.
        cuentaPasos = 0

    #Movimiento hacia adelante acelerando
    if acelera:   
        ventana.blit(acelerando[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    elif salto + 1 >= 1:
        ventana.blit(salta,(int(px), int(py)))
        cuentaPasos += 1

    else:
       ventana.blit(quieto,(int(px), int(py)))


#Cargamos el sprite de moto
Moto_sprite = pygame.image.load("Imagenes/Moto.png").convert_alpha()

def recorte_imagen (a,b,c,d):
    
    global Moto_sprite
    
    #Moto_sprite = pygame.image.load("Imagenes/Personaje_Sprite.png").convert_alpha()  #Cargamos la imagen con los movimientos
    Moto_sprite.set_clip(pygame.Rect(a,b,c,d))  
    Moto_1 = Moto_sprite.subsurface(Moto_sprite.get_clip())
    Ancho_moto = Moto_1.get_size()
    MotoBig = pygame.transform.scale(Moto_1,(int(Ancho_moto[0]*2),(Ancho_moto[1]*2)))
    return MotoBig





#Variables para usar los obstaculos----------------------------------------------------------------------------------------------------------------------

#El iterador para pasar las imagenes de las sierras
iteradorObstaculo=0



#Variables
FPS =45 #creamos la variable para la cantidad de pixeles a la que queremos que se mueva el fondo
reloj=pygame.time.Clock() # hacemos el reloj para determinar cada cuanto se actualiza
variables = Variables_CargaImagenes() # En el objeto variables, guardamos las variables para mover el fondo y el piso

#Imagenes para los movimientos del personaje

quieto = pygame.image.load("Imagenes/Moto1.png")


#0,115,106,62
    #106,115,105,57
    #213,115,105,57
    #318,115,105,57

acelerando = [ recorte_imagen(0,115,106,62),
               recorte_imagen(106,115,105,57),
               recorte_imagen(213,115,105,57),
               recorte_imagen(318,115,105,57)  
          ]

salta = pygame.image.load("Imagenes/Moto1.png")

#----------------------------------------------------------

#Variables del personaje:

#Para poder ubicarlo en la pantalla
x=0
px = 0
py = 500
ancho = 40
velocidad = 10

#Variables para que pueda realizar el salto
salto= False
#Altura del salto
cuentaSalto = 13

#Variables de accion
acelera = True     #Apretar Intro para que inicie a correr la moto.



#------------------------------Inicializamos variables globales ---------------------------------------

#Pasos
cuentaPasos = 0



global contadorVelocidad
contadorVelocidad = 0
global contadorObstaculo
contadorObstaculo = 0
global cambiarObstaculo
cambiarObstaculo = 0

velocidad_a = False



#--------------------------------------------------------------------------------Comienza el bucle donde se ejecuta el juego-----------------------------------------

# Bucle principal
while True:
    #logicaPiso()
    #dibujarPiso()
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    #Opción tecla pulsada
    keys = pygame.key.get_pressed()

    

    #Personaje quieto 
    if acelera != True : # Cuando toque un obstaculo ponemos acelera en false.
        acelera = False
        cuentaPasos = 0
          
    
    #Tecla SPACE - Salto
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            cuentaPasos = 0
    else:
        if cuentaSalto >= -13:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.2
            cuentaSalto -= 1
        else:
            cuentaSalto = 13
            salto = False


    #Generamos el piso y el fondo movil.
    
    
    cargar_fondo()     #Controlamos la velocidad del fondo
    cargar_piso()      #Controlamos la velocidad del piso 
    obstaculo()        #Controlamos la aparicion y cambio de obstaculos  
    movimiento_moto()  #Movimiento de la moto 
    puntuacion()        

    
    contadorVelocidad +=1
    contadorObstaculo +=1
    #hace que cada vez se mueva mas rapido, aumentando la dificultad
    if contadorVelocidad == 100: #estaba en 200, que cambia??  -- Es la cantidad de vueltas que tiene que hacer el bucle, para aumentar en 0,01 la velocidad del piso. 
       velocidad_a = True 
       contadorVelocidad = 0 
       
    
    if contadorVelocidad%100==0: #estaba en 200, que cambia??
        cambiarObstaculo= 1
    if contadorObstaculo>400:
         cambiarObstaculo= 0
         contadorObstaculo=0
    
    #contador de puntos --cuanto mas alto sea el numero del multiplo mas lento suma los puntos
    if(contadorVelocidad%9==0):
        variables.puntos+=1
       


    pygame.display.update()  # Para actualizar la pantalla
    reloj.tick(FPS)  #Definimos la cantidad de FPS a la que queremos que vaya el juego



    
    