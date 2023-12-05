# * Reto #21
# * CALCULADORA .TXT
# * Fecha publicación enunciado: 23/05/22
# * Fecha publicación resolución: 01/06/22
# * Dificultad: MEDIA
# *
# * Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
# * - El .txt se corresponde con las entradas de una calculadora.
# * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
# * - Soporta números enteros y decimales.
# * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
# * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
# * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

from io import TextIOWrapper


def solucion():
    try:
        listSaltos: list[str] = AperturaArchivo()
        listSaltos: list[str] = borrandoSaltos(listSaltos)
        print(NumerosoOperadores(listSaltos))
    except ValueError:
        print("No se han podido resolver las operaciones")

def borrandoSaltos(listaValores: list[str])-> list[str]:
    listaValores: list[str] = listaValores.replace("\n", " ")
    listaValores: list[str] = listaValores.split(" ")
    return listaValores

def NumerosoOperadores(listaValores: list[str])-> int:
    numero1: float = 0
    operacion: str = ""
    contador: int = 0
    total: float = 0

    for valor in listaValores:
        if contador == 0:
            numero1 = float(valor)
        if contador == 1:
            operacion = valor
        if contador == 2:
            contador = 0
            if operacion == "+":
                total += numero1 + float(valor)
            if operacion == "-":
                total += numero1 - float(valor)
            if operacion == "*":
                total += numero1 * float(valor)
            if operacion == "/":
                total += numero1 / float(valor)
        contador += 1
    return total

def AperturaArchivo()-> list[str]:
    archivo: TextIOWrapper = open(file='Challenge21.txt',mode= 'r')
    contenido: str = archivo.read()
    archivo.close()
    return contenido


if __name__ == '__main__':
    solucion()