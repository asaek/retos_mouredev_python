# * Reto #23
# * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
# * Fecha publicación enunciado: 07/06/22
# * Fecha publicación resolución: 13/06/22
# * Dificultad: MEDIA
# *
# * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
# * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.


def MaximoComunDivisor(numero1: int, numero2: int )-> int:
    while numero2:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1
def MinimoComunMultiplo(numero1: int, numero2: int )-> int:
    return (numero1 * numero2) / MaximoComunDivisor(numero1=numero1, numero2=numero2)

if __name__ == "__main__":
    print(MaximoComunDivisor(numero1=56, numero2=180))
    print(MinimoComunMultiplo(numero1=56, numero2=180))