import tkinter as tk
from tkinter import messagebox
import pygame

class JuegoInterfaz:
    def __init__(self, master, game_logic):
        self.master = master
        self.game_logic = game_logic

        self.click_sound = pygame.mixer.Sound("Musica/multi-pop-1-188165.mp3")
        self.win_sound = pygame.mixer.Sound("Musica/collect-points-190037.mp3")
        self.draw_sound = pygame.mixer.Sound("Musica/negative_beeps-6008.mp3")

        self.click_sound.set_volume(0.3)
        self.win_sound.set_volume(0.3)
        self.draw_sound.set_volume(0.3)

        self.configurar_interfaz()

        self.label_nombre_j1 = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_nombre_j1.grid(row=0, column=0, pady=10, padx=10)

        self.label_nombre_j2 = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_nombre_j2.grid(row=0, column=2, pady=10, padx=10)

        self.label_victorias_j1 = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_victorias_j1.grid(row=1, column=0, pady=10, padx=10)

        self.label_victorias_j2 = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_victorias_j2.grid(row=1, column=2, pady=10, padx=10)

        self.botones = self.crear_botones()

        self.label_resultado = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_resultado.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

        self.btn_reiniciar = tk.Button(self.master, text="Reiniciar Partida", font=('Arial', 14),
                                       command=self.reiniciar_partida, state=tk.DISABLED,
                                       bg="#543C33", fg="white", activebackground="#382B20", activeforeground="white")
        self.btn_reiniciar.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

        self.actualizar_interfaz()

    def configurar_interfaz(self):
        self.master.title("Tres en Raya")
        self.master.configure(bg="#f0f0f0")
        self.master.geometry("580x790")
        self.master.resizable(False, False)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_rowconfigure(5, weight=1)
        self.master.grid_rowconfigure(6, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

    def crear_botones(self):
        botones = []
        for i in range(3):
            for j in range(3):
                boton = tk.Button(self.master, text="", font=('Arial', 30), width=6, height=3,
                                  command=lambda fila=i, col=j: self.jugar(fila, col),
                                  bg="#F7E7CE", fg="#543C33", activebackground="#E0CDA9")
                boton.grid(row=i + 2, column=j, padx=10, pady=10)
                botones.append(boton)
        return botones

    def jugar(self, fila, col):
        if self.game_logic.chequear_ganador() is None:
            resultado = self.game_logic.jugar(fila, col)
            self.click_sound.play()
            self.actualizar_tablero()
            if resultado:
                if resultado == "Empate":
                    self.label_resultado.config(text="¡Es un empate!")
                    self.draw_sound.play()
                else:
                    nombre_ganador = self.game_logic.jugadores[0] if resultado == 'X' else self.game_logic.jugadores[1]
                    self.label_resultado.config(text=f"¡{nombre_ganador} ha ganado!")
                    self.win_sound.play()
                self.actualizar_victorias()
                self.btn_reiniciar.config(state=tk.NORMAL)
                if resultado != "Empate":
                    for boton in self.botones:
                        boton.config(state=tk.DISABLED)
            else:
                self.actualizar_turno()
                if self.game_logic.vs_ia and self.game_logic.turno == 1:
                    for boton in self.botones:
                        boton.config(state=tk.DISABLED)
                    self.master.after(1000, self.jugar_ia)


    def jugar_ia(self):
        resultado = self.game_logic.jugar_ia()
        self.click_sound.play()
        self.actualizar_tablero()
        if resultado:
            if resultado == "Empate":
                self.label_resultado.config(text="¡Es un empate!")
                self.draw_sound.play()
            else:
                nombre_ganador = self.game_logic.jugadores[0] if resultado == 'X' else self.game_logic.jugadores[1]
                self.label_resultado.config(text=f"¡{nombre_ganador} ha ganado!")
                self.win_sound.play()
            self.actualizar_victorias()
            self.btn_reiniciar.config(state=tk.NORMAL)
            if resultado != "Empate":
                for boton in self.botones:
                    boton.config(state=tk.DISABLED)
        else:
            self.actualizar_turno()
            for boton in self.botones:
                boton.config(state=tk.NORMAL)

    def actualizar_tablero(self):
        for i in range(3):
            for j in range(3):
                self.botones[i * 3 + j].config(text=self.game_logic.tablero[i][j])

    def actualizar_turno(self):
        self.label_resultado.config(text=f"Turno de: {self.game_logic.jugadores[self.game_logic.turno]}")

    def actualizar_victorias(self):
        self.label_victorias_j1.config(text=f"Victorias {self.game_logic.jugadores[0]}: {self.game_logic.victorias[0]}")
        self.label_victorias_j2.config(text=f"Victorias {self.game_logic.jugadores[1]}: {self.game_logic.victorias[1]}")

    def actualizar_interfaz(self):
        self.label_nombre_j1.config(text=f"{self.game_logic.jugadores[0]} (X):")
        self.label_nombre_j2.config(text=f"{self.game_logic.jugadores[1]} (O):")
        self.label_resultado.config(text=f"Comienza {self.game_logic.jugadores[self.game_logic.turno]}")
        self.master.deiconify()

    def reiniciar_partida(self):
        self.label_resultado.config(text="")
        self.game_logic.reiniciar_juego()
        self.actualizar_tablero()
        self.actualizar_turno()
        for boton in self.botones:
            boton.config(state=tk.NORMAL)
        self.btn_reiniciar.config(state=tk.DISABLED)


def validar_longitud(valor):
    if len(valor) <= 7:
        return True
    else:
        return False


class IngresoNombres(tk.Toplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.parent = parent
        self.callback = callback
        self.vs_ia = False
        self.configurar_ventana()

        self.label_jugador1 = tk.Label(self, text="Ingrese el nombre del Jugador 1 (X):", font=('Arial', 14),
                                       bg="#f0f0f0", fg="#543C33")
        self.label_jugador1.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.entry_jugador1 = tk.Entry(self, font=('Arial', 14), validate='key')
        self.entry_jugador1['validatecommand'] = (self.entry_jugador1.register(validar_longitud), '%P')
        self.entry_jugador1.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.label_jugador2 = tk.Label(self, text="Ingrese el nombre del Jugador 2 (O):", font=('Arial', 14),
                                       bg="#f0f0f0", fg="#543C33")
        self.label_jugador2.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.entry_jugador2 = tk.Entry(self, font=('Arial', 14), validate='key')
        self.entry_jugador2['validatecommand'] = (self.entry_jugador2.register(validar_longitud), '%P')
        self.entry_jugador2.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.checkbox_vs_ia = tk.Checkbutton(self, text="Jugar contra la IA", font=('Arial', 14), bg="#f0f0f0",
                                             fg="#543C33", command=self.toggle_vs_ia)
        self.checkbox_vs_ia.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        self.btn_confirmar = tk.Button(self, text="Confirmar", font=('Arial', 14), bg="#543C33", fg="white",
                                       command=self.on_confirmar, activebackground="#382B20", activeforeground="white")
        self.btn_confirmar.grid(row=2, columnspan=2, padx=10, pady=10)

    def toggle_vs_ia(self):
        self.vs_ia = not self.vs_ia
        if self.vs_ia:
            self.entry_jugador2.config(state=tk.DISABLED, disabledbackground="#d3d3d3", disabledforeground="grey")
            self.entry_jugador2.delete(0, tk.END)
        else:
            self.entry_jugador2.config(state=tk.NORMAL, disabledbackground=self.cget('bg'), disabledforeground="black")

    def configurar_ventana(self):
        self.title("Ingreso de Nombres")
        self.configure(bg="#f0f0f0")
        self.geometry("600x150")
        self.resizable(False, False)
        self.update_idletasks()
        self.centrar_ventana()

    def centrar_ventana(self):
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def on_confirmar(self):
        nombre_jugador1 = self.entry_jugador1.get()
        nombre_jugador2 = self.entry_jugador2.get() if not self.vs_ia else "IA"
        if nombre_jugador1 and (nombre_jugador2 or self.vs_ia):
            self.callback()
        else:
            messagebox.showerror("Error", "Debe ingresar nombres para ambos jugadores")

    def obtener_nombres(self):
        return [self.entry_jugador1.get(), self.entry_jugador2.get() if not self.vs_ia else "IA"]












