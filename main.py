from game import Game

g = Game()

while g.funcionando:
    g.menu_actual.display_menu()  #invocamos al menu principal
    g.loop_juego()

    