import pygame,sys
from pygame.locals import *

#------------Colores------------------------
Color =pygame.Color(70,80,150)
Verde =pygame.Color(0, 255, 126)
Gris = pygame.Color(165, 172, 171)
Amarillo = pygame.Color(243, 254, 0)
Azul = pygame.Color(0, 51, 254)
Blanco = pygame.Color(255, 255, 255)
Negro = pygame.Color(0,0,0)
#------------inicio de ventana y configuracion del pygame------------------------

pygame.init()
ANCHO = 800 
LARGO = 600
ventana=pygame.display.set_mode((ANCHO,LARGO))
pygame.display.set_caption("Primer jogo")
gameExit = False
reloj = pygame.time.Clock()
click = False

#fuenteChica=pygame.font.Font("fuentes/E-BRAIN2.TTF",25)   #letra1 para el menu
fuenteChica=pygame.font.Font("fuentes/EagleGTII.ttf",25)   #letra2 de marca ruedas para menu o titulo
#fuenteChica=pygame.font.SysFont("comicsansms", 15)        #letra3 comun para menu
fuenteMediana=pygame.font.SysFont("comicsansms", 30)
fuenteGrande=pygame.font.SysFont("comicsansms", 80)

#------------Tamaño de los botones------------------------
tamBoton=[200,50]
#------------Boton de jugar-------------------------------
Boton=[50,100]
ColorBotonJugar=[Gris,Azul]
#------------Boton de Creditos-------------------------------
BotonCreditos=[50,200]
ColorBotonCreditos=[Gris,Amarillo]
#------------Boton de Opciones-------------------------------
BotonOpciones=[50,300]
ColorBotonOpciones=[Gris,Azul]
#------------Boton salir----------------------------------
BotonSalir=[50,400]
ColorBotonSalir=[Gris,Amarillo]


def botones(ventana,color,pos,tam):
    boton= pygame.draw.rect(ventana,color[1],(pos[0],pos[1],tam[0],tam[1]))
    return boton

def objetotexto(texto,color,tamanio):
    if tamanio=="pequenio":
        textoSuperficie=fuenteChica.render(texto,True,color)
    if tamanio=="mediano":
        textoSuperficie=fuenteMediana.render(texto,True,color)
    if tamanio=="grande":
        textoSuperficie=fuenteGrande.render(texto,True,color)
    
    return textoSuperficie, textoSuperficie.get_rect()

def TextoDeBoton(msg,color,BotonX,BotonY,Ancho,Alto,tamanio="pequenio"):
    textoSuperficie, textoRect = objetotexto(msg,color,tamanio)
    textoRect.center = (BotonX + (Ancho/2),BotonY+(Alto/2))
    ventana.blit(textoSuperficie,textoRect)




# pygame.draw.line(ventana, Color, (60,80), (160,100),50) Dibujamos lineas
""" pygame.draw.circle(ventana,(29,51,243),(80,90),250)
pygame.draw.circle(ventana,(252,18,18),(150,310),250)

pygame.draw.rect(ventana,(0,0,0),(150,70,130,45))
pygame.draw.rect(ventana,(0,100,200),(155,77,120,32))

pygame.draw.rect(ventana,(0,0,0),(150,140,130,45))
pygame.draw.rect(ventana,(0,100,200),(155,147,120,32))

pygame.draw.rect(ventana,(0,0,0),(150,210,130,45))
pygame.draw.rect(ventana,(0,100,200),(155,217,120,32)) """


""" while not gameExit:
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            gameExit = True """

fuente = pygame.font.SysFont(None, 20)
pygame.font.get_fonts
def mostrar_texto(text, font, color, surface, x, y):
    textoObjeto = font.render(text,1,color)
    textrect = textoObjeto.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textoObjeto, textrect)


def main_menu():
    mostrar_texto('Menu Principal',fuente,(255,255,255),ventana,20,20)
    pygame.mixer.music.load('Sonidos/dale-boca.mp3')
    pygame.mixer.music.play(1)
    while True:

        fondo = pygame.image.load("Imagenes/bobo.jpg").convert()
        ventana.blit(fondo, (0, 0))
        
        mx, my = pygame.mouse.get_pos()
        opcion_1 = pygame.Rect(50,100,200,50)
        opcion_2 = pygame.Rect(50,200,200,50)

        

        if opcion_1.collidepoint((mx,my)):
            if click:
                juego()
        if opcion_2.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        #pygame.draw.rect(ventana,(255,0,0),opcion_1)
        #pygame.draw.rect(ventana,(255,0,0),opcion_2)
        botones(ventana,ColorBotonJugar,Boton,tamBoton)
        botones(ventana,ColorBotonCreditos,BotonCreditos,tamBoton)
        botones(ventana,ColorBotonOpciones,BotonOpciones,tamBoton)
        botones(ventana,ColorBotonSalir,BotonSalir,tamBoton)
        TextoDeBoton("Iniciar",Blanco,Boton[0],Boton[1],tamBoton[0],tamBoton[1])
        TextoDeBoton("Salir",Negro,BotonCreditos[0],BotonCreditos[1],tamBoton[0],tamBoton[1])
        TextoDeBoton("Creditos",Negro,BotonSalir[0],BotonSalir[1],tamBoton[0],tamBoton[1])
        TextoDeBoton("Opciones",Blanco,BotonOpciones[0],BotonOpciones[1],tamBoton[0],tamBoton[1])

        #mostrar_texto('Jugar',fuente,(255,255,255),ventana,115,120)
        #mostrar_texto('Salir',fuente,(255,255,255),ventana,115,220)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                
        pygame.display.update()
        reloj.tick(60)

def juego():
    seguir = True
    while seguir:
        ventana.fill((0,0,0))
        mostrar_texto('Juego',fuente,(255,255,255),ventana,20,20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    seguir = False

        pygame.display.update()
        reloj.tick(60)

main_menu()



        

