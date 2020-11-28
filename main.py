from game import Game

# Guardar en una variable la clase Game()

g = Game()



while g.funcionando:
    g.menu_actual.display_menu()  #invocamos al menu principal
    
    # Una vez que elejimos el mapa, inicia el loop del juego
     
    g.loop_juego()

    