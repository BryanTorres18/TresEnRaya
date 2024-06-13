import tkinter as tk
from juego_logica import JuegoLogica
from juego_interfaz import JuegoInterfaz, IngresoNombres

def empezar_juego():
    nombres = ingreso_nombres.obtener_nombres()
    if nombres:
        game_logic.jugadores = nombres
        game_board = JuegoInterfaz(root, game_logic)
        ingreso_nombres.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tres en Raya")
    root.configure(bg="#f0f0f0")

    game_logic = JuegoLogica()
    ingreso_nombres = IngresoNombres(root, empezar_juego)

    root.mainloop()


