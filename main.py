import tkinter as tk
from juego_logica import JuegoLogica
from juego_interfaz import JuegoInterfaz, IngresoNombres
import pygame

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def empezar_juego():
    nombres = ingreso_nombres.obtener_nombres()
    if nombres:
        game_logic.jugadores = nombres[:2] if not ingreso_nombres.vs_ia else [nombres[0], f"IA ({ingreso_nombres.dificultad.get()[0]})"]
        game_logic.vs_ia = ingreso_nombres.vs_ia
        game_logic.dificultad = ingreso_nombres.obtener_dificultad()
        game_board = JuegoInterfaz(root, game_logic)
        root.deiconify()
        centrar_ventana(root, 580, 790)
        ingreso_nombres.destroy()
        pygame.mixer.music.play(-1)

        if game_logic.vs_ia and game_logic.turno == 1:
            game_board.master.after(1000, game_board.jugar_ia)

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.music.load("Musica/game-music-loop-6-144641.mp3")
    pygame.mixer.music.set_volume(0.2)
    root = tk.Tk()
    root.title("Tres en Raya")
    root.configure(bg="#f0f0f0")
    root.withdraw()

    game_logic = JuegoLogica()
    ingreso_nombres = IngresoNombres(root, empezar_juego)
    centrar_ventana(ingreso_nombres, 580, 270)

    root.mainloop()
    pygame.quit()



