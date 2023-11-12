# * Reto #14
# * ¿ES UN NÚMERO DE ARMSTRONG?
# * Fecha publicación enunciado: 04/04/22
# * Fecha publicación resolución: 11/04/22
# * Dificultad: FÁCIL
# *
# * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
# * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.


def main(numero : int):
    if numero < 0:
        print('No pueden ser numeros negativos')
        return
    digitos: int = cantidadDigititos(numero=numero)
    listDigitos = separarDigitos(numero)
    sumaDIgitos: int = 0
    for digito in listDigitos:
        sumaDIgitos += digito ** digitos
    if numero == sumaDIgitos:
        print('Si es un numero Amstrong Narcisista')
    else:
        print('No es un numero Amstrong narcisista')

def separarDigitos(numero: int) -> list[int]:
    listDigitos : list[int] = [int (digito) for digito in str(numero)]
    return listDigitos

def cantidadDigititos(numero: int) -> int:
    digitos: int = 0
    while numero > 0:
        numero //= 10
        digitos += 1
    return digitos

if __name__ == '__main__':
    main(numero=-371)