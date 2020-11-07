import pygame
from game import *
import os

class Menu():
    def __init__(self, game):
        self.game=game
        self.mitad_ancho, self.mitad_alto = self.game.ANCHO / 2, self.game.LARGO / 2
        self.correr_pantalla = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.cursor_rectDer = pygame.Rect(0, 0, 20, 20)
        self.offset = -130 #aca es un atributo fijo,lo llamamos cuando dibujamos el asterisco para que este -100 pixeles del texto del menu
        self.offder = 150
        self.fondo_inicial=pygame.image.load("Imagenes/FondoInicial.jpg").convert()
        
    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)
        self.game.draw_text('*', 15, self.cursor_rectDer.x, self.cursor_rectDer.y)

    def blit_screen(self):
        self.game.ventana.blit(self.game.pantalla, (0, 0))  #mostramos el menu, dibuja una imagen sobre la otra
        pygame.display.update() #actualizamos
        self.game.reiniciar_tecla() #reiniciamos las teclas a False para que el cursor no se mueva solo

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"    #ponemos el estado en start para el comienzo del menu
        self.startx, self.starty = self.mitad_ancho, self.mitad_alto + 30  # posicionamos el x y el y de start
        self.opcionesx, self.opcionesy = self.mitad_ancho, self.mitad_alto + 50  #hacemos lo mismo que lo de arriba pero sumandole 20 a la altura
        self.creditsx, self.creditsy = self.mitad_ancho, self.mitad_alto + 70  #lo mismo que antes
        self.salirx, self.saliry = self.mitad_ancho, self.mitad_alto + 90
        self.recordx, self.recordy = self.mitad_ancho, self.mitad_alto + 130
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  #dibujamos el asterisco de la izquierda 
        self.cursor_rectDer.midtop = (self.startx + self.offder,self.starty) #dibujamos el asterisco de la izquierda
        self.partida="Iniciar Partida"
        self.numero =0
    def display_menu(self):
        self.correr_pantalla = True
        pygame.mixer.music.load('Sonidos/pokemon.mp3')
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(1)

        #Obtenemos el record actual del jugador del "highscore.txt para poder mostrarlo en la pantalla principal"

        if os.stat("highscore.txt").st_size == 0:
            self.numero = 0 
        else:
            self.numero = self.game.max_score() #Obtenemos el record actual del usuario.

        #---------------------------------------------------------------------------------------------------------

        while self.correr_pantalla:
            self.game.comprobar_evento()    #comprobamos si se presiono una tecla o la x de la ventana para salir
            self.check_input()
            self.game.pantalla.blit(self.fondo_inicial, (0, 0)) #mostramos la imagen del fondo de menu
            self.game.draw_text('Menu principal', 20, self.game.ANCHO / 2, self.game.LARGO / 2 - 150)
            self.game.draw_text(self.partida, 20, self.startx, self.starty)
            self.game.draw_text("Record Actual " + str(self.numero), 25, self.recordx, self.recordy) #Mostramos el record actual.
            self.game.draw_text("Opciones", 20, self.opcionesx, self.opcionesy)
            self.game.draw_text("Creditos", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Salir", 20, self.salirx, self.saliry)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):  #esta funcion dibujamos el asterisco
        if self.game.DOWN_KEY:  #preguntamos si apretamos la flecha de abajo
            if self.state == 'Start':   #si la presinamos y el estado es Start dibujamos el asterisco en opciones
                self.cursor_rect.midtop = (self.opcionesx + self.offset, self.opcionesy)
                self.cursor_rectDer.midtop = (self.opcionesx + self.offder, self.opcionesy)
                self.state = 'Options'  # cambiamos el estado a opciones
            elif self.state == 'Options':   
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.cursor_rectDer.midtop = (self.creditsx + self.offder, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.salirx + self.offset, self.saliry)
                self.cursor_rectDer.midtop = (self.salirx + self.offder, self.saliry)
                self.state = 'Salir'
            elif self.state == 'Salir':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.cursor_rectDer.midtop = (self.startx + self.offder, self.starty)
                self.state = 'Start'


        elif self.game.UP_KEY:  #preguntamos si apretamos la flecha de arriba
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.salirx + self.offset, self.saliry)
                self.cursor_rectDer.midtop = (self.salirx + self.offder, self.saliry)
                self.state = 'Salir'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.cursor_rectDer.midtop = (self.startx + self.offder, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.opcionesx + self.offset, self.opcionesy)
                self.cursor_rectDer.midtop = (self.opcionesx + self.offder, self.opcionesy)
                self.state = 'Options'
            elif self.state == 'Salir':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.cursor_rectDer.midtop = (self.creditsx + self.offder, self.creditsy)
                self.state = 'Credits'

                

    def check_input(self):
        self.move_cursor()  #dibujamos el asterisco en la posicion a medida que vamos subiendo o bajando
        if self.game.START_KEY: #si apretamos la tecla enter ingresamos a start, opciones, creditos o salir.
            if self.state == 'Start': #si el estado es start jugando es igual a true  
                self.game.jugando= True
                self.game.menu_actual=self.game.mapas
            elif self.state == 'Options':   #sino preguntamos si el estado es options 
                self.game.menu_actual = self.game.options #ingresamos al menu de opciones
            elif self.state == 'Credits':   #sino preguntamos si el estado es credits
                self.game.menu_actual = self.game.credits #ingresamos al menu de creditos
            elif self.state == 'Salir':
                self.game.menu_actual = self.game.cartelExit
                #self.game.menu_actual = self.game.salir
            elif self.state == 'Mapas':
                self.game.menu_actual = self.game.mapas
            self.correr_pantalla = False
            
    # Hacer cartel 
    #if self.opcion == 'Atras': # sino, volvemos al menu principal
                #self.game.menu_actual = self.game.main_menu
    #self.game.menu_actual = self.game.salir #Salir definitivo del juego








class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mitad_ancho, self.mitad_alto + 20
        self.controlsx, self.controlsy = self.mitad_ancho, self.mitad_alto + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)  #dibujamos el cursor de la izquierda
        self.cursor_rectDer.midtop = (self.volx + self.offder, self.voly)   #dibujamos el cursor de la derecha
        self.atrasx, self.atrasy = self.game.ANCHO / 2, self.controlsy + 20

    def display_menu(self):
        self.correr_pantalla = True

        while self.correr_pantalla:
            self.game.comprobar_evento()
            self.check_input()
            self.game.pantalla.blit(self.fondo_inicial, (0, 0)) #mostramos la imagen del fondo de menu
            self.game.draw_text('Opciones', 20, self.game.ANCHO / 2, self.game.LARGO / 2 - 150)
            self.game.draw_text("Volumen", 15, self.volx, self.voly)
            self.game.draw_text("Controles", 15, self.controlsx, self.controlsy)
            self.game.draw_text("ATRAS", 15, self.game.ANCHO / 2, self.controlsy + 20) 
            self.draw_cursor()
            self.blit_screen()

    def check_input(self): #Dibujar los asteriscos a los costados.
        
        if self.game.START_KEY: #Tecla enter
            if self.state=="Atras":
                if self.game.esMenu=="Iniciar":
                    self.game.menu_actual = self.game.main_menu
                elif self.game.esMenu=="Continuar":
                    self.game.menu_actual = self.game.pausaMenu    
            elif self.state=='Controls':
                self.game.menu_actual=self.game.controles
            elif self.state == 'Volume':
                self.game.menu_actual = self.game.volumen #Ingresamos al menu, del volumen?
            self.correr_pantalla = False

        elif self.game.UP_KEY: #Tecla para ir para arriba
            if self.state == 'Volume': #Para saber en que opcion estas parado.
                self.state = 'Atras'
                self.cursor_rect.midtop = (self.atrasx + self.offset, self.atrasy)
                self.cursor_rectDer.midtop = (self.atrasx + self.offder, self.atrasy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.cursor_rectDer.midtop = (self.volx + self.offder, self.voly)
            elif self.state == 'Atras':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.cursor_rectDer.midtop = (self.controlsx + self.offder, self.controlsy)
                
        elif self.game.DOWN_KEY: #Tecla para ir para abajo
            if self.state == 'Volume': #Para saber en que opcion estas parado.
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.cursor_rectDer.midtop = (self.controlsx + self.offder, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Atras'
                self.cursor_rect.midtop = (self.atrasx + self.offset, self.atrasy)
                self.cursor_rectDer.midtop = (self.atrasx + self.offder, self.atrasy)
            elif self.state == 'Atras':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.cursor_rectDer.midtop = (self.volx + self.offder, self.voly)

        
            

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.cursor_rect.midtop = (self.game.ANCHO / 2 + self.offset, self.game.LARGO / 2 + 120)  #dibujamos el cursor de la izquierda
        self.cursor_rectDer.midtop = (self.game.ANCHO / 2 + self.offder, self.game.LARGO / 2 + 120)   #dibujamos el cursor de la derecha

    def display_menu(self):
        self.correr_pantalla = True
        while self.correr_pantalla: #esperamos si se presiona el enter o borrar seteamos el corre_pantalla
            self.game.comprobar_evento()
            if self.game.START_KEY or self.game.BACK_KEY:   # si le damos a enter o a borrar volvemos al menu principal
                if self.game.esMenu=="Iniciar":
                    self.game.menu_actual = self.game.main_menu
                elif self.game.esMenu=="Continuar":
                    self.game.menu_actual = self.game.pausaMenu   # volvemos al menu principal
                self.correr_pantalla = False    # seteamos la variable para salir del bucle
            self.game.pantalla.blit(self.fondo_inicial, (0, 0)) #mostramos la imagen del fondo de menu
            self.game.draw_text('Creditos', 20, self.game.ANCHO / 2, self.game.LARGO / 2 - 150)  #mostramos el titulo del menu
            self.game.draw_text('Alan Signetti', 15, self.game.ANCHO / 2 -4, self.game.LARGO / 2 + 10) #mostramos la persona
            self.game.draw_text('Cristian Scarella', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 30) #mostramos la persona 
            self.game.draw_text('Yago Rexach', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 50) #mostramos la persona
            self.game.draw_text('Fernando Scroppo', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 70) #mostramos la persona
            self.game.draw_text('ATRAS', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 120) 
            self.draw_cursor()
            self.blit_screen()
class SalirMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.game.funcionando=False


class PausaMenu(MainMenu):
    def __init__(self, game):
        MainMenu.__init__(self,game)
        self.partida="Continuar"


class VolumenMenu(OptionsMenu):
    def __init__(self, game):
        OptionsMenu.__init__(self,game)
        self.cursor_rect.midtop = (self.game.ANCHO / 2 + self.offset, self.game.LARGO / 2 + 150)  #dibujamos el cursor de la izquierda
        self.cursor_rectDer.midtop = (self.game.ANCHO / 2 + self.offder, self.game.LARGO / 2 + 150)   #dibujamos el cursor de la derecha
        
        self.V_max = pygame.image.load("Imagenes/vol_3_transparente.png") 
        self.V_2 = pygame.image.load("Imagenes/vol_2_transparente.png")
        self.V_1 = pygame.image.load("Imagenes/vol_1_transparente.png")
        self.V_mute = pygame.image.load("Imagenes/vol_mute.png")

        self.volumen = [
                self.V_mute,
                self.V_1,
                self.V_2,
                self.V_max
                    ]

        self.iterador=2

    def display_menu(self):
        self.correr_pantalla = True
        resto = 0.04

        self.game.pantalla.blit(self.volumen[self.iterador],(390,110))  #Imagen por defecto

        while self.correr_pantalla: #esperamos si se presiona el enter o borrar seteamos el corre_pantalla
            

            self.game.pantalla.blit(self.fondo_inicial, (0, 0))
            self.game.draw_text('Volumen', 20, self.game.ANCHO / 2, 67)  #mostramos el titulo del menu
            self.game.draw_text('ATRAS', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 150) 
            


            self.game.comprobar_evento()
            if self.game.START_KEY:  # si le damos a enter volvemos al menu principal
                self.game.menu_actual = self.game.options
                self.correr_pantalla = False    # seteamos la variable para salir del bucle 

            elif self.game.LEFT_KEY and self.game.sonido.get_volume()>0:
                redondeo_volumen_actual = round(self.game.sonido.get_volume(),2)  #Obtenemos 
                round_resta = round ((redondeo_volumen_actual - resto),2)
                self.game.sonido.set_volume(round_resta)
                self.iterador = self.iterador-1
                

            elif self.game.RIGHT_KEY and round(self.game.sonido.get_volume(),2) <0.12:
                redondeo_volumen_actual = round(self.game.sonido.get_volume(),2)
                round_resta = round ((redondeo_volumen_actual + resto),2)
                self.game.sonido.set_volume(round_resta)
                self.iterador = self.iterador+1

            self.game.pantalla.blit(self.volumen[self.iterador],(390,110))  

            # Mute: 0.00 Nivel 1: 0.04 nivel 2: 0.08  max: 0.12 



            self.draw_cursor()
            self.blit_screen()



class ControlesMenu(OptionsMenu):
    def __init__(self, game):
        OptionsMenu.__init__(self,game)
        self.cursor_rect.midtop = (self.game.ANCHO / 2 + self.offset, self.game.LARGO / 2 + 200)  #dibujamos el cursor de la izquierda
        self.cursor_rectDer.midtop = (self.game.ANCHO / 2 + self.offder, self.game.LARGO / 2 + 200)   #dibujamos el cursor de la derecha


    def display_menu(self):
        self.correr_pantalla = True
        while self.correr_pantalla: #esperamos si se presiona el enter o borrar seteamos el corre_pantalla
            self.game.comprobar_evento()
            if self.game.START_KEY:  # si le damos a enter volvemos al menu principal
            #    """  if self.game.esMenu=="Iniciar":
                self.game.menu_actual = self.game.options
            #     elif self.game.esMenu=="Continuar":
            #         self.game.menu_actual = self.game.pausaMenu """   # volvemos al menu principal
                self.correr_pantalla = False    # seteamos la variable para salir del bucle
            self.game.pantalla.blit(self.fondo_inicial, (0, 0)) #mostramos la imagen del fondo de menu
            self.game.draw_text('Controles', 20, self.game.ANCHO / 2, 67)  #mostramos el titulo del menu
            self.game.draw_text('ATRAS', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 200) 

            # Cargamos las imagenes de los controles y describimos sus funciones

            #Configuracion de la tecla enter
            T_enter = pygame.image.load("Imagenes/t_enter.png")
            T_enter = pygame.transform.scale(T_enter,(64,64))
            self.game.pantalla.blit(T_enter,(435,130)) #Posicion de la tecla
            self.game.draw_text('Selecionar Opcion', 19,660, 161)  #Accion de la tecla
            
            #Configuracion del espacio
            T_espacio = pygame.image.load("Imagenes/T_espacio.png")
            T_espacio = pygame.transform.scale(T_espacio,(107,65))
            self.game.pantalla.blit(T_espacio,(395,200))
            self.game.draw_text('Saltar', 19,570, 230)

            #Configuracion de la tecla escape
            T_escape = pygame.image.load("Imagenes/T_escape.png")
            self.game.pantalla.blit(T_escape,(442,270))
            self.game.draw_text('Menu de pausa', 19,635, 300)

            #Configuracion de la tecla p
            T_p = pygame.image.load("Imagenes/T_p.png")
            self.game.pantalla.blit(T_p,(442,340))
            self.game.draw_text('Pausa / Reintentar', 19,670, 370)

            #Configuracion de las flechas de seleccion
            t_flechas = pygame.image.load("Imagenes/flechas_navegacion.png")
            self.game.pantalla.blit(t_flechas,(442,410))
            self.game.draw_text('Flechas de navegacion', 19,700, 440)

            #Configuracion de las flechas de subir y bajar volumen
            t_volumen = pygame.image.load("Imagenes/T_volumen.png")
            self.game.pantalla.blit(t_volumen,(380,480))
            self.game.draw_text('Bajar / Subir Volumen', 19,700, 495)    

            self.draw_cursor()
            self.blit_screen()


class MapasMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state="Mapa 1"
        self.opcion= "Seleccionar"
        self.seleccionarx,self.seleccionary=self.mitad_ancho, self.mitad_alto + 120
        self.atrasx,self.atrasy=self.mitad_ancho, self.mitad_alto + 140
        self.cursor_rect.midtop = (self.seleccionarx+ self.offset, self.seleccionary)  #dibujamos el cursor de la izquierda
        self.cursor_rectDer.midtop = (self.seleccionarx + self.offder, self.seleccionary)   #dibujamos el cursor de la derecha  
        self.mostrar_menu=True
        self.fondo_previo=pygame.image.load("Imagenes/City3.jpg").convert()
        self.mapa=pygame.image.load("Imagenes/City3.jpg").convert()
        self.game= game
        self.sonido_mapa = 1
        self.piso = pygame.image.load("Imagenes/Piso_Mapa_2.jpg").convert()
       
        
        
    def display_menu(self):
        self.correr_pantalla = True
        
        while self.correr_pantalla: #esperamos si se presiona el enter o borrar seteamos el corre_pantalla
            self.game.comprobar_evento()
            self.check_input()
            self.game.pantalla.blit(self.fondo_inicial, (0, 0)) #mostramos la imagen del fondo de menu
            self.game.draw_text('Mapas', 20, self.game.ANCHO / 2, 67)  #mostramos el titulo del menu
            self.game.draw_text('Seleccionar', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 120) 
            self.game.draw_text('Atras', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 140) 
            self.fondo_previo=pygame.transform.scale(self.fondo_previo,(325,200)) #Achica la imagen del mapa
            self.game.pantalla.blit(self.fondo_previo,(500,200)) #mostramos los mapas para la eleccion
            self.draw_cursor()
            self.blit_screen()
            

    def check_input(self): 
        
        if self.game.START_KEY:  # si le damos a enter volvemos al menu principal
            if self.opcion == 'Seleccionar': #preguntamos si apretamos enter y seleccionamos el mapa entonces vamos al juego
                self.eleccion()
                self.comprobar_sonido() # Carga el sonido de acuerdo al mapa seleccionado
                self.mostrar_menu = False
            if self.opcion == 'Atras': # sino, volvemos al menu principal
                self.game.menu_actual = self.game.main_menu
            self.correr_pantalla = False    # seteamos la variable para salir del bucle

        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.opcion == 'Seleccionar':
                self.opcion = 'Atras'
                self.cursor_rect.midtop = (self.atrasx + self.offset, self.atrasy)
                self.cursor_rectDer.midtop = (self.atrasx + self.offder, self.atrasy)
            elif self.opcion == 'Atras':
                self.opcion = 'Seleccionar'
                self.cursor_rect.midtop = (self.seleccionarx + self.offset, self.seleccionary)
                self.cursor_rectDer.midtop = (self.seleccionarx + self.offder, self.seleccionary)
        
        elif self.game.RIGHT_KEY or self.game.LEFT_KEY: 
            if self.state == 'Mapa 1': #Para saber en que opcion estas parado.
                self.state = 'Mapa 2'
                self.fondo_previo=pygame.image.load("Imagenes/City2.jpg")
            elif self.state == 'Mapa 2':
                self.state = 'Mapa 1'
                self.fondo_previo=pygame.image.load("Imagenes/City3.jpg")
    
    def eleccion(self):
        if self.state == 'Mapa 1':
            self.mapa=pygame.image.load("Imagenes/City3.jpg")
            self.obstaculo = pygame.image.load("Imagenes/Pincho.png")
            #self.game.sonido = self.musica_mapa[0] 
            self.piso = pygame.image.load("Imagenes/piso22.jpg").convert()
            
            
        elif self.state == 'Mapa 2':
            self.mapa=pygame.image.load("Imagenes/City2.jpg")
            self.obstaculo = pygame.image.load("Imagenes/barril.png")
            # = self.musica_mapa[1]
            self.piso = pygame.image.load("Imagenes/Piso_Mapa_2.jpg").convert()

    def comprobar_sonido (self): 
        # Carga el sonido de acuerdo al mapa seleccionado por el jugador.
        
        if(self.state == 'Mapa 1' and self.sonido_mapa == 2 ):
            
            self.game.sonido = pygame.mixer.Sound("Sonidos/juego.wav")
            self.game.sonido.set_volume(0.08)
            self.sonido_mapa = 1
        elif (self.state == 'Mapa 2' and self.sonido_mapa == 1 ):
            
            self.game.sonido = pygame.mixer.Sound("Sonidos/Mapa_2.wav")
            self.game.sonido.set_volume(0.08)
            self.sonido_mapa = 2


class CartelExit(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.opcion= "Si"
        self.six,self.siy=self.mitad_ancho, self.mitad_alto + 70
        self.nox,self.noy=self.mitad_ancho, self.mitad_alto + 90
        self.cursor_rect.midtop = (self.six+ self.offset, self.siy)  #dibujamos el cursor de la izquierda
        self.cursor_rectDer.midtop = (self.six + self.offder, self.siy)   #dibujamos el cursor de la derecha  
        self.game= game
        
       
        
        
    def display_menu(self):
        self.correr_pantalla = True
        
        while self.correr_pantalla: #esperamos si se presiona el enter o borrar seteamos el corre_pantalla
            self.game.comprobar_evento()
            self.check_input()
            #self.game.pantalla.fill(self.game.Negro)   # Establecemos de color negro la pantalla
            pygame.draw.rect(self.game.pantalla,self.game.Rojo, pygame.Rect((480,320, 320, 150)),0) #Dibujamos el rectangulo de fondo
            #self.game.draw_text('Salir', 20, self.game.ANCHO / 2, 67)  #mostramos el titulo del menu
            self.game.draw_text('Estas seguro que', 20, self.game.ANCHO / 2, 340)
            self.game.draw_text('deseas salir', 20, self.game.ANCHO / 2, 370)
            self.game.draw_text('Si', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 70) 
            self.game.draw_text('No', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 90) 
            self.draw_cursor()
            self.blit_screen()
            pygame.display.update()

    def check_input(self): 
        
        if self.game.START_KEY:  # si le damos a enter volvemos al menu principal
            if self.opcion == 'Si': #Si la opcion es "Si" salimos definitivamente del juego.
                self.game.menu_actual = self.game.salir
            if self.opcion == 'No': # sino, volvemos al menu principal
                self.game.menu_actual = self.game.main_menu
            self.correr_pantalla = False    # seteamos la variable para salir del bucle

        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.opcion == 'Si':
                self.opcion = 'No'
                self.cursor_rect.midtop = (self.nox + self.offset, self.noy)
                self.cursor_rectDer.midtop = (self.nox + self.offder, self.noy)
            elif self.opcion == 'No':
                self.opcion = 'Si'
                self.cursor_rect.midtop = (self.six + self.offset, self.siy)
                self.cursor_rectDer.midtop = (self.six + self.offder, self.siy)
        
        

            
