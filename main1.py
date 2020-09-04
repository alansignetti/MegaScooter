# Importamos todos los modulos de pygame
import pygame,sys
from pygame.locals import *

# Inicializamos todos los modulos de pygame
pygame.init()

# Variable para las ventanas 
ANCHO = 1280
LARGO = 720
Blanco = pygame.Color(255, 255, 255)


ventana = pygame.display.set_mode((ANCHO, LARGO))
fuente_Puntuacion=pygame.font.Font("fuentes/8-BIT WONDER.TTF",25)


# QUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE???




#Colocar el titulo a la ventana
pygame.display.set_caption("MegaScooter")

# class Piso():
#     def __init__(self):
#         self.x=0        #inicializacion en 0
#         self.y=100

# class Nivel():
#     def __init__(self):
#         self.velocidad=-6

# velocidad=Nivel()
# pisoNuevo=Piso()
# def dibujarPiso():
#     piso = pygame.image.load("Imagenes/piso1.jpg").convert()   #cargamos la imagen en variable fondo
#     ventana.blit(piso, (pisoNuevo.x, 500))

# def logicaPiso():
    
#     if(pisoNuevo.x<-800):  #-- -900 Si no llega a -800 resta 2px al costado la imagen
#         pisoNuevo.x=800  # -- 100+ANCHO
#     else:
#         pisoNuevo.x+=velocidad.velocidad

# En esta clase vamos a guardar las variables que utilizamos para hacer el fondo y el piso movil.
class Variables_CargaImagenes():

    def __init__(self):
         self.xPiso=0       
         self.xFondo=0
         self.numeroVelocidad=15
         self.puntos=0

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
        variables.numeroVelocidad += 0.05/50

    piso = pygame.image.load("Imagenes/piso22.jpg").convert()   #cargamos la imagen en variable piso
    x_rel_Piso= variables.xPiso % piso.get_rect().width  #despues del % el comando obtiene el ancho
    #de la foto siendo el divisor de xPiso devuelve el resto

    ventana.blit(piso, (x_rel_Piso-piso.get_rect().width, altoPiso))
    if(x_rel_Piso<ANCHO):
        ventana.blit(piso,(x_rel_Piso,altoPiso)) #Mostramos la imagen
        variables.xPiso-=variables.numeroVelocidad #Calcula la velocidad mientras el numero sea mas alto mas rapido ira el movimiento de la imagen
    # xPiso es la cantidad de pixeles por segundo

    #-----------------------------FinPiso-------------------------------------------

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



#Variables
FPS =45 #creamos la variable para la cantidad de pixeles a la que queremos que se mueva el fondo
reloj=pygame.time.Clock() # hacemos el reloj para determinar cada cuanto se actualiza
variables = Variables_CargaImagenes() # En el objeto variables, guardamos las variables para mover el fondo y el piso

#Imagenes para los movimientos del personaje

quieto = pygame.image.load("Imagenes/Moto1.png")

acelerando = [ pygame.image.load('Imagenes/Moto1.png'),
            pygame.image.load('Imagenes/Moto2.png'),
            pygame.image.load('Imagenes/Moto3.png'),
            pygame.image.load('Imagenes/Moto4.png')
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
cuentaSalto = 11

#Variables de accion
acelera = True     #Apretar Intro para que inicie a correr la moto.

#Pasos
cuentaPasos = 0


global contadorVelocidad
contadorVelocidad = 0
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



    #Tecla Enter - La moto arranca y comienza 

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
        if cuentaSalto >= -11:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 11
            salto = False


    #Generamos el piso y el fondo movil.
    
    
    cargar_fondo()
    cargar_piso()
    movimiento_moto()
    puntuacion()

    contadorVelocidad +=1
    #hace que cada vez se mueva mas rapido, aumentando la dificultad
    if contadorVelocidad == 10: #estaba en 200, que cambia??
       velocidad_a = True 
       contadorVelocidad = 0 
    
    #contador de puntos --cuanto mas alto sea el numero del multiplo mas lento suma los puntos
    if(contadorVelocidad%9==0):
        variables.puntos+=1
       


    pygame.display.update()  # Para actualizar la pantalla
    reloj.tick(FPS)  #Definimos la cantidad de FPS a la que queremos que vaya el juego



    
    