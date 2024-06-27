import random

class JuegoLogica:
    def __init__(self):
        self.reiniciar_juego()
        self.jugadores = ["", ""]
        self.victorias = [0, 0]
        self.vs_ia = False
        self.dificultad = 0.3

    def jugar(self, fila, col):
        if self.tablero[fila][col] == "":
            self.tablero[fila][col] = "X" if self.turno == 0 else "O"
            ganador = self.chequear_ganador()
            if ganador and ganador != "Empate":
                self.victorias[self.turno] += 1
            self.turno = 1 - self.turno
            return ganador
        return None

    def jugar_ia(self):
        if random.random() < self.dificultad:
            movimientos_posibles = [(i, j) for i in range(3) for j in range(3) if self.tablero[i][j] == ""]
            mejor_movimiento = random.choice(movimientos_posibles)
        else:
            mejor_movimiento = self.minimax(self.tablero, True)[1]

        if mejor_movimiento:
            self.tablero[mejor_movimiento[0]][mejor_movimiento[1]] = "O"
            ganador = self.chequear_ganador()
            if ganador and ganador != "Empate":
                self.victorias[self.turno] += 1
            self.turno = 1 - self.turno
            return ganador

    def minimax(self, tablero, es_maximizador):
        ganador = self.chequear_ganador()
        if ganador:
            if ganador == "X":
                return -1, None
            elif ganador == "O":
                return 1, None
            elif ganador == "Empate":
                return 0, None

        if es_maximizador:
            mejor_valor = -float('inf')
            mejor_movimiento = None
            for i in range(3):
                for j in range(3):
                    if tablero[i][j] == "":
                        tablero[i][j] = "O"
                        valor = self.minimax(tablero, False)[0]
                        tablero[i][j] = ""
                        if valor > mejor_valor:
                            mejor_valor = valor
                            mejor_movimiento = (i, j)
            return mejor_valor, mejor_movimiento
        else:
            mejor_valor = float('inf')
            mejor_movimiento = None
            for i in range(3):
                for j in range(3):
                    if tablero[i][j] == "":
                        tablero[i][j] = "X"
                        valor = self.minimax(tablero, True)[0]
                        tablero[i][j] = ""
                        if valor < mejor_valor:
                            mejor_valor = valor
                            mejor_movimiento = (i, j)
            return mejor_valor, mejor_movimiento

    def chequear_ganador(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] and self.tablero[i][0] != "":
                return self.tablero[i][0]
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] and self.tablero[0][i] != "":
                return self.tablero[0][i]

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] and self.tablero[0][0] != "":
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] and self.tablero[0][2] != "":
            return self.tablero[0][2]

        for fila in self.tablero:
            for casilla in fila:
                if casilla == "":
                    return None
        return "Empate"

    def reiniciar_juego(self):
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.turno = 0









