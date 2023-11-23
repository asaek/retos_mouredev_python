# * Reto #18
# * TRES EN RAYA
# * Fecha publicación enunciado: 02/05/22
# * Fecha publicación resolución: 09/05/22
# * Dificultad: DIFÍCIL
# *
# * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
# * - "X" si han ganado las "X"
# * - "O" si han ganado los "O"
# * - "Empate" si ha habido un empate
# * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
# * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
from enum import Enum

class TicTacToeValue(Enum):
    X = 1
    O = 2
    EMPTY = 3
def main(partida: list[list[TicTacToeValue]]):

    isCorrect: bool = conteoTiros(partida=partida)
    if not isCorrect:
        print("Esta mal el juego")
        return

    # Comparacion por fila
    for fila in partida:
        cantidadX: int = 0
        cantidadO: int = 0
        for slot in fila:
            if slot == TicTacToeValue.X:
                cantidadX += 1
            elif slot == TicTacToeValue.O:
                cantidadO += 1
            if cantidadX == 3:
                print('Gano: X')
                return
            if cantidadO == 3:
                print('Gano: O')
                return

    # Comparacion por Columna
    numWhile: int = 0
    while numWhile < 3:
        cantidadX: int = 0
        cantidadO: int = 0
        for i in range(0, 3):
            # print(partida[i][numWhile])
            if partida[i][numWhile] == TicTacToeValue.X:
                cantidadX += 1
            elif partida[i][numWhile] == TicTacToeValue.O:
                cantidadO += 1
            if cantidadX == 3:
                print('Gano: X')
                return
            if cantidadO == 3:
                print('Gano: O')
                return
        numWhile += 1

    # Comparacion por esquineado
    numWhileX: int = 0
    cantidadX: int = 0
    cantidadO: int = 0
    while numWhileX < 3:
        # print(partida[numWhileX][numWhileX])

        if partida[numWhileX][numWhileX] == TicTacToeValue.X:
            cantidadX += 1
        elif partida[numWhileX][numWhileX] == TicTacToeValue.O:
            cantidadO += 1
        if cantidadX == 3:
            print('Gano: X')
            return
        if cantidadO == 3:
            print('Gano: O')
            return
        numWhileX += 1

    numWhileX: int = 0
    numWhileY: int = 2
    cantidadX: int = 0
    cantidadO: int = 0
    while numWhileX < 3:
        print(partida[numWhileX][numWhileY])

        if partida[numWhileX][numWhileY] == TicTacToeValue.X:
            cantidadX += 1
        elif partida[numWhileX][numWhileY] == TicTacToeValue.O:
            cantidadO += 1
        if cantidadX == 3:
            print('Gano: X')
            return
        if cantidadO == 3:
            print('Gano: O')
            return
        numWhileX += 1
        numWhileY -= 1

    print('Empate!!!')




def conteoTiros (partida: list[list[TicTacToeValue]]) -> bool:
    cantidadX: int = 0
    cantidadO: int = 0
    for fila in partida:
        for slot in fila:
            if slot == TicTacToeValue.X:
                cantidadX += 1
            if slot == TicTacToeValue.O:
                cantidadO += 1
    if cantidadX < cantidadO:
        if cantidadO - 1 != cantidadX:
            return False
    if cantidadO < cantidadX:
        if cantidadX - 1 != cantidadO:
            return False
    return True

if __name__ == '__main__':
    main(
        [[TicTacToeValue.X, TicTacToeValue.O, TicTacToeValue.O],
         [TicTacToeValue.O, TicTacToeValue.X, TicTacToeValue.X],
         [TicTacToeValue.O, TicTacToeValue.X, TicTacToeValue.X]]
    )