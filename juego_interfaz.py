import tkinter as tk
from tkinter import messagebox

class JuegoInterfaz:
    def __init__(self, master, game_logic):
        self.master = master
        self.game_logic = game_logic

        self.master.title("Tres en Raya")
        self.master.configure(bg="#f0f0f0")

        self.label_nombre_j1 = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_nombre_j1.grid(row=0, column=0, pady=10, padx=10)

        self.label_nombre_j2 = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_nombre_j2.grid(row=0, column=2, pady=10, padx=10)

        self.label_victorias_j1 = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_victorias_j1.grid(row=1, column=0, pady=10, padx=10)

        self.label_victorias_j2 = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_victorias_j2.grid(row=1, column=2, pady=10, padx=10)

        self.botones = []
        for i in range(3):
            for j in range(3):
                boton = tk.Button(self.master, text="", font=('Arial', 20), width=6, height=3,
                                  command=lambda fila=i, col=j: self.jugar(fila, col),
                                  bg="#F7E7CE", fg="#543C33", activebackground="#E0CDA9")
                boton.grid(row=i + 2, column=j, padx=10, pady=10)
                self.botones.append(boton)

        self.label_resultado = tk.Label(self.master, text="", font=('Arial', 16), bg="#f0f0f0", fg="#543C33")
        self.label_resultado.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

        self.btn_reiniciar = tk.Button(self.master, text="Reiniciar Partida", font=('Arial', 14),
                                       command=self.reiniciar_partida, state=tk.DISABLED, bg="#543C33", fg="white",
                                       activebackground="#382B20", activeforeground="white")
        self.btn_reiniciar.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

        self.actualizar_interfaz()

    def jugar(self, fila, col):
        if self.game_logic.chequear_ganador() is None:
            resultado = self.game_logic.jugar(fila, col)
            if resultado:
                self.actualizar_tablero()
                if resultado == "Empate":
                    self.label_resultado.config(text="¡Es un empate!")
                else:
                    self.label_resultado.config(text=f"¡{resultado} ha ganado!")
                self.actualizar_victorias()
                self.btn_reiniciar.config(state=tk.NORMAL)
                if resultado != "Empate":
                    for boton in self.botones:
                        boton.config(state=tk.DISABLED)
            else:
                self.actualizar_tablero()
                self.actualizar_turno()

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
        self.master.withdraw()

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


class IngresoNombres(tk.Toplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.parent = parent
        self.callback = callback
        self.title("Ingreso de Nombres")
        self.configure(bg="#f0f0f0")

        self.label_jugador1 = tk.Label(self, text="Ingrese el nombre del Jugador 1 (X):", font=('Arial', 14), bg="#f0f0f0", fg="#543C33")
        self.label_jugador1.grid(row=0, column=0, padx=10, pady=10)
        self.entry_jugador1 = tk.Entry(self, font=('Arial', 14))
        self.entry_jugador1.grid(row=0, column=1, padx=10, pady=10)

        self.label_jugador2 = tk.Label(self, text="Ingrese el nombre del Jugador 2 (O):", font=('Arial', 14), bg="#f0f0f0", fg="#543C33")
        self.label_jugador2.grid(row=1, column=0, padx=10, pady=10)
        self.entry_jugador2 = tk.Entry(self, font=('Arial', 14))
        self.entry_jugador2.grid(row=1, column=1, padx=10, pady=10)

        self.btn_confirmar = tk.Button(self, text="Confirmar", font=('Arial', 14), bg="#543C33", fg="white", command=self.on_confirmar, activebackground="#382B20", activeforeground="white")
        self.btn_confirmar.grid(row=2, columnspan=2, padx=10, pady=10)

    def on_confirmar(self):
        nombre_jugador1 = self.entry_jugador1.get()
        nombre_jugador2 = self.entry_jugador2.get()
        if nombre_jugador1 and nombre_jugador2:
            self.callback()
        else:
            messagebox.showerror("Error", "Debe ingresar nombres para ambos jugadores")

    def obtener_nombres(self):
        return [self.entry_jugador1.get(), self.entry_jugador2.get()]










