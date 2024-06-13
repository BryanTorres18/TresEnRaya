import random

class JuegoLogica:
    def __init__(self):
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.turno = random.randint(0, 1)  # Se elige aleatoriamente quién comienza
        self.jugadores = ["", ""]
        self.victorias = [0, 0]

    def jugar(self, fila, col):
        if self.tablero[fila][col] == "":
            self.tablero[fila][col] = "X" if self.turno == 0 else "O"
            ganador = self.chequear_ganador()
            if ganador and ganador != "Empate":
                self.victorias[self.turno] += 1
            self.turno = 1 - self.turno
            return ganador
        else:
            return None

    def chequear_ganador(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != "":
                return self.tablero[i][0]
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != "":
                return self.tablero[0][i]
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != "":
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != "":
            return self.tablero[0][2]
        if all(all(row) for row in self.tablero):
            return "Empate"
        return None

    def reiniciar_juego(self):
        self.turno = random.randint(0, 1)  # Se elige aleatoriamente quién comienza
        self.tablero = [["" for _ in range(3)] for _ in range(3)]







