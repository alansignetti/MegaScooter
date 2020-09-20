import pygame

class Menu():
    def __init__(self, game):
        self.game=game
        self.mitad_ancho, self.mitad_alto = self.game.ANCHO / 2, self.game.LARGO / 2
        self.correr_pantalla = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.cursor_rectDer = pygame.Rect(0, 0, 20, 20)
        self.offset = -130 #aca es un atributo fijo,lo llamamos cuando dibujamos el asterisco para que este -100 pixeles del texto del menu
        self.offder = 150
        
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
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  #dibujamos el asterisco de la izquierda 
        self.cursor_rectDer.midtop = (self.startx + self.offder,self.starty) #dibujamos el asterisco de la izquierda
    def display_menu(self):
        self.correr_pantalla = True
        while self.correr_pantalla:
            self.game.comprobar_evento()    #comprobamos si se presiono una tecla o la x de la ventana para salir
            self.check_input()
            self.game.pantalla.fill(self.game.Negro)
            self.game.draw_text('Menu principal', 20, self.game.ANCHO / 2, self.game.LARGO / 2 - 20)
            self.game.draw_text("Iniciar Partida", 20, self.startx, self.starty)
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
            elif self.state == 'Options':   #sino preguntamos si el estado es options 
                self.game.menu_actual = self.game.options #ingresamos al menu de opciones
            elif self.state == 'Credits':   #sino preguntamos si el estado es credits
                self.game.menu_actual = self.game.credits #ingresamos al menu de creditos
            elif self.state == 'Salir':
                self.game.menu_actual = self.game.salir
            self.correr_pantalla = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mitad_ancho, self.mitad_alto + 20
        self.controlsx, self.controlsy = self.mitad_ancho, self.mitad_alto + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)  #dibujamos el cursor de la izquierda
        self.cursor_rectDer.midtop = (self.volx + self.offder, self.voly)   #dibujamos el cursor de la derecha

    def display_menu(self):
        self.correr_pantalla = True
        while self.correr_pantalla:
            self.game.comprobar_evento()
            self.check_input()
            self.game.pantalla.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.ANCHO / 2, self.game.LARGO / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.menu_actual = self.game.main_menu
            self.correr_pantalla = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.cursor_rectDer.midtop = (self.controlsx + self.offder, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.cursor_rectDer.midtop = (self.volx + self.offder, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            # falta crear el menu de volumen y mostrar los controles
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.correr_pantalla = True
        while self.correr_pantalla: #esperamos si se presiona el enter o borrar seteamos el corre_pantalla
            self.game.comprobar_evento()
            if self.game.START_KEY or self.game.BACK_KEY:   # si le damos a enter o a borrar volvemos al menu principal
                self.game.menu_actual = self.game.main_menu   # volvemos al menu principal
                self.correr_pantalla = False    # seteamos la variable para salir del bucle
            self.game.pantalla.fill(self.game.Negro)   # Establecemos de color negro la pantalla
            self.game.draw_text('Creditos', 20, self.game.ANCHO / 2, self.game.LARGO / 2 - 20)  #mostramos el titulo del menu
            self.game.draw_text('Persona 1', 15, self.game.ANCHO / 2 -4, self.game.LARGO / 2 + 10) #mostramos la persona
            self.game.draw_text('Persona 2', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 30) #mostramos la persona 
            self.game.draw_text('Persona 3', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 50) #mostramos la persona
            self.game.draw_text('Persona 4', 15, self.game.ANCHO / 2, self.game.LARGO / 2 + 70) #mostramos la persona

            self.blit_screen()

class SalirMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.game.funcionando=False