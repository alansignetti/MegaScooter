# Importamos todos los modulos de pygame
import pygame,sys
from pygame.locals import *
from menu import *


class Game():
    def __init__(self):
        #pygame.init()
        self.reiniciar_juego()
        
        
    def reiniciar_juego(self):
        self.funcionando, self.jugando = True, False
        self.Color,self.Verde,self.Gris,self.Amarillo,self.Azul,self.Blanco,self.Negro=(70,80,150),(0, 255, 126),(165, 172, 171),(243, 254, 0),(0, 51, 254),(255, 255, 255),(0,0,0)
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY,self.P_KEY = False,False, False, False, False, False
        #self.ANCHO,self.LARGO=1280,720
        #self.pantalla = pygame.Surface((self.ANCHO,self.LARGO))
        #self.ventana=pygame.display.set_mode((self.ANCHO, self.LARGO))
        self.fuente_Puntuacion='fuentes/8-BIT WONDER.TTF'
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.salir = SalirMenu(self)
        self.menu_actual = self.main_menu
        self.titulo=pygame.display.set_caption("MegaScooter")
        self.xPiso=0       
        self.xFondo=0
        self.numeroVelocidad=15
        self.puntos=0
        self.xobstaculo = 1280
        self.yobstaculo = 540
        self.resta=15
        self.FPS =45
        self.reloj=pygame.time.Clock()
        self.velocidad_a=False
        self.acelera = True
        self.salto= False
        self.cuentaPasos = 0
        self.contadorVelocidad =0
        self.puntos=0
        self.cuentaSalto = 13
        self.px = 0
        self.py=500
        self.tam_fuente_puntos=25
        self.pausa=False
        self.iteradorObstaculo=0
        self.cambiarObstaculo=0
        self.contadorObstaculo=0
        self.acelerando = []
        self.Moto_sprite = pygame.image.load("Imagenes/Moto.png")  
        self.perder=False
        
        
    pygame.init()
    ANCHO,LARGO=1280,720
    pantalla = pygame.Surface((ANCHO,LARGO))
    ventana=pygame.display.set_mode((ANCHO,LARGO))

    # tuve que cambiarlo del init porque sino, no me toma el sprite de la moto .convert_alpha()
    

    #Videos para hacer el fondo y el piso movil https://www.youtube.com/watch?v=Ftln3VrFV6s&list=PLVzwufPir356RMxSsOccc38jmxfxqfBdp&index=4   

    def loop_juego(self):
        if(self.jugando):
            self.mute()
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.load('Sonidos/juego.mp3')
            pygame.mixer.music.play(1)

        while self.jugando:
            
            self.comprobar_evento()
            if self.ESCAPE_KEY:  #si apretamos enter el juego vuelve al menu
                self.jugando= False
            elif self.P_KEY:    # si apretamos la "p" muestra el carter de pausa
                self.mute() #muteamos la cancion 
                self.pausar()  #mostramos mensaje de pausa
                self.unmute()  #volvemos a escuchar la cancion
            

                

            #Opción tecla pulsada
            keys = pygame.key.get_pressed()

            

            #Personaje quieto 
            if self.acelera != True : # Cuando toque un obstaculo ponemos acelera en false.
                self.acelera = False
                self.cuentaPasos = 0
                
            
            #Tecla SPACE - Salto
            if not (self.salto):
                if keys[pygame.K_SPACE]:
                    self.salto = True
                    self.cuentaPasos = 0
            else:
                if self.cuentaSalto >= -13:
                    self.py -= (self.cuentaSalto * abs(self.cuentaSalto)) * 0.2
                    self.cuentaSalto -= 1
                   
                else:
                    self.cuentaSalto = 13
                    self.salto = False


            #Generamos el piso y el fondo movil.
            
            
            self.cargar_fondo()
            self.cargar_piso()
            self.obstaculo()
            self.movimiento_moto()
            self.puntuacion()
            self.colisiones()
            #self.ventana.blit(self.Marcador,(self.xobstaculo,self.yobstaculo))
            


            self.contadorVelocidad +=1
            self.contadorObstaculo +=1
            #hace que cada vez se mueva mas rapido, aumentando la dificultad
            if self.contadorVelocidad == 100: #estaba en 200, que cambia??  -- Es la cantidad de vueltas que tiene que hacer el bucle, para aumentar en 0,01 la velocidad del piso. 
                self.velocidad_a = True 
                self.contadorVelocidad  = 0 
            
            
            if(self.contadorVelocidad %100==0): #estaba en 200, que cambia??
                self.puntos+=1
                #self.cambiarObstaculo= 1
            if self.contadorObstaculo>400:
                self.cambiarObstaculo= 0
                self.contadorObstaculo=0


            #contador de puntos --cuanto mas alto sea el numero del multiplo mas lento suma los puntos
            if(self.contadorVelocidad%9==0):
                self.puntos+=1

            self.reiniciar_tecla()
            pygame.display.update()
            self.reloj.tick(self.FPS)
    
    def mute(self):
        pygame.mixer.music.pause()
    
    def unmute(self):
        pygame.mixer.music.unpause()

    def reiniciar_tecla(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY,self.P_KEY = False,False,False, False, False, False
            

    
    def comprobar_evento(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.funcionando, self.jugando = False, False
                self.menu_actual.correr_pantalla = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY= True
                if event.key == pygame.K_p:
                    self.P_KEY= True
                    
            
    def pausar(self):
        self.pausa=True
        while self.pausa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pausa=False
            fuente=pygame.font.Font(self.fuente_Puntuacion,self.tam_fuente_puntos)
            pygame.draw.rect(self.ventana,self.Negro, pygame.Rect((635,350, 135, 50)),0)
            texto_de_pausa=fuente.render("PAUSA",True,self.Blanco)
            self.ventana.blit(texto_de_pausa,(self.ANCHO/2,self.LARGO/2))
            pygame.display.update()
            
            
            self.reiniciar_tecla()
            

        

    def cargar_fondo(self):
        #-----------------------------Fondo----------------------------------------------
        fondo= pygame.image.load("Imagenes/City3.jpg").convert()
        x_rel_Fondo= self.xFondo % fondo.get_rect().width  # Hacemos el valor de "x" dividido "%" el ancho del fondo "fondo.get_rect().width"
        self.ventana.blit(fondo, (x_rel_Fondo - fondo.get_rect().width, 0))

        # Este if permite que el fondo se repita indefinidamente
        if(x_rel_Fondo<self.ANCHO):
            self.ventana.blit(fondo,(x_rel_Fondo,0))
        self.xFondo-=8  #Cambias la velocidad del fondo.
        #----------------------------Fin Fondo-------------------------------------------





    def cargar_piso (self):
        #-------------------------------Piso-------------------------------------------
        altoPiso = 597 #Calculamos el alto del piso
        

        if self.velocidad_a == True:
            self.numeroVelocidad += 0.05/50

        piso = pygame.image.load("Imagenes/piso22.jpg").convert()   #cargamos la imagen en variable piso

        #pincho= pygame.image.load("Imagenes/Pincho.png") #Agregamos la imagen del obstaculo

        x_rel_Piso= self.xPiso % piso.get_rect().width  #despues del % el comando obtiene el ancho
        #de la foto siendo el divisor de xPiso devuelve el resto

        self.ventana.blit(piso, (x_rel_Piso-piso.get_rect().width, altoPiso))
        if(x_rel_Piso<self.ANCHO):
            self.ventana.blit(piso,(x_rel_Piso,altoPiso)) #Mostramos la imagen
            self.xPiso-=self.numeroVelocidad
        # xPiso es la cantidad de pixeles por segundo

        #-----------------------------FinPiso-------------------------------------------

    def obstaculo (self):
        if self.cambiarObstaculo==1:
            vobstaculo=[pygame.image.load('Imagenes/Sierras1.png'),
                        pygame.image.load('Imagenes/Sierras2.png'),
                        pygame.image.load('Imagenes/Sierras3.png'),
                        pygame.image.load('Imagenes/Sierras4.png')
                        ] 

            if self.iteradorObstaculo + 1 >= 4: #Este iterador recorre las 4 imagenes de la sierra
                self.iteradorObstaculo = 0 
                
            self.xobstaculo = self.xobstaculo - self.resta  
            self.ventana.blit(vobstaculo[self.iteradorObstaculo // 1], (int(self.xobstaculo), int(self.yobstaculo)))
            self.iteradorObstaculo += 1

            if self.xobstaculo <= -200 : 
                self.xobstaculo = 1280
                self.resta +=0.5


        else:
            vobstaculo= pygame.image.load("Imagenes/Pincho.png") #Agregamos la imagen del obstaculo

            if self.xobstaculo >= -100:    #Un if desplaza el obstaculo hacia la izquierda y cuando llega al final, lo devuelve al principio.
                
                self.xobstaculo = self.xobstaculo - self.resta
                self.ventana.blit (vobstaculo,(self.xobstaculo,self.yobstaculo)) 

            else:
                self.xobstaculo = 1280 #Cuando el obstaculo llegue a la punta izquierda, setea la variable para ponerlo al principio. 
                self.resta +=0.5  #En cuanto queres que se incremente cada vez que vuelva a aparecer de vuelta el obstaculo


    def colisiones (self):
     
       if self.xobstaculo >5 and self.xobstaculo <180 and self.py>480 and self.py<501: # and self.py>499 and self.py<1000
            self.perder=True
            while self.perder:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.perder=False
                            self.reiniciar_juego()
                            
                            
                fuentePerder=pygame.font.Font(self.fuente_Puntuacion,self.tam_fuente_puntos)

                
                
                
                
                # dibuja el rectángulo
                pygame.draw.rect(self.ventana,self.Negro, pygame.Rect((590,350, 200, 50)),0)    #pygame.Rect (x,y,ancho,alto) dibujar un rectangulo
                pygame.draw.rect(self.ventana,self.Negro, pygame.Rect((515,500, 350, 70)),0)
                texto_de_pausa=fuentePerder.render("Perdiste",True,self.Blanco)
                texto_de_pausa_2 = fuentePerder.render("Presiona P para",True,self.Blanco)
                texto_de_pausa_3 = fuentePerder.render("*REINTENTAR*",True,self.Blanco)
                self.ventana.blit(texto_de_pausa,(600,360))
                self.ventana.blit(texto_de_pausa_2,(520,500))
                self.ventana.blit(texto_de_pausa_3,(560,540))
                pygame.display.update()
                #pygame.quit()
                #sys.exit()
            self.reiniciar_juego()     





    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.fuente_Puntuacion,size)
        text_surface = font.render(text, True, self.Blanco)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.pantalla.blit(text_surface,text_rect)


    
    def recorte_imagen (self,a,b,c,d,imagen):


        self.Moto_sprite.set_clip(pygame.Rect(a,b,c,d))  
        Moto_1 = self.Moto_sprite.subsurface(self.Moto_sprite.get_clip())
        Ancho_moto = Moto_1.get_size()
        MotoBig = pygame.transform.scale(Moto_1,(int(Ancho_moto[0]*2),(Ancho_moto[1]*2)))
        return MotoBig
    
    


    def puntuacion(self):
        fuente_PuntuacionPar=pygame.font.Font(self.fuente_Puntuacion,self.tam_fuente_puntos)
        texto_de_puntos=fuente_PuntuacionPar.render("Puntos "+str(self.puntos),True,self.Blanco)
        self.ventana.blit(texto_de_puntos,(900,15))


    quieto = pygame.image.load("Imagenes/Moto1.png")
    salta = pygame.image.load("Imagenes/Moto1.png")
    
    def movimiento_moto (self):

        #-----------------------------Logica para mover la moto-------------------------------
        #Variables globales
        #global cuentaPasos
        global x

        #global Moto_sprite = pygame.image.load("Imagenes/Moto.png")

        self.acelerando = [
                            self.recorte_imagen(0,115,106,62,self.Moto_sprite),
                            self.recorte_imagen(106,115,105,57,self.Moto_sprite),
                            self.recorte_imagen(213,115,105,57,self.Moto_sprite),
                            self.recorte_imagen(318,115,105,57,self.Moto_sprite)  
                    ]


        
        #Estos if anidados definen segun la tecla que se aprete las imagenes que se tiene que mostrar

        #Contador de pasos
        if self.cuentaPasos + 1 >= 4:   #>= 4 porque las fotos del movimiento de la moto son 4.
            self.cuentaPasos = 0

        #Movimiento hacia adelante acelerando
        if self.acelera:   
            self.ventana.blit(self.acelerando[self.cuentaPasos // 1], (int(self.px), int(self.py)))
            self.cuentaPasos += 1

        elif self.salto + 1 >= 1:
            self.ventana.blit(self.salta,(int(self.px), int(self.py)))
            self.cuentaPasos += 1

        else:
            self.ventana.blit(self.quieto,(int(self.px), int(self.py)))


    
    
    
