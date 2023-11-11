# * Reto #13
# * FACTORIAL RECURSIVO
# * Fecha publicación enunciado: 28/03/22
# * Fecha publicación resolución: 04/04/22
# * Dificultad: FÁCIL
# *
# * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def main(numeroFact: int, factorial: int = 1):
    print(factorial)
    if numeroFact > 1:
        factorial = factorial * numeroFact
        main(numeroFact= numeroFact - 1, factorial= factorial )

def main2(factorial: int ) -> int:
    if factorial < 0:
        return 0
    elif factorial <= 1:
        return 1
    else:
        print(factorial * (main2(factorial - 1)))
        return factorial * (main2(factorial - 1))




if __name__ == '__main__':
    # main(numeroFact=5,)
    print(main2(factorial=5))