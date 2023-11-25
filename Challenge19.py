# * Reto #19
# * CONVERSOR TIEMPO
# * Fecha publicación enunciado: 09/05/22
# * Fecha publicación resolución: 16/05/22
# * Dificultad: FACIL
# *
# * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def solucion(dias: int = 0, horas: int  = 0, minutos: int  = 0, segundos: int = 0) -> int:
    milisegundos: int = 0
    if segundos != 0:
        milisegundos = segundos * 1000
    if minutos != 0:
        milisegundos += minutos * 60000
    if horas != 0:
        milisegundos += horas * 3600000
    if dias != 0:
        milisegundos += dias * 86400000
    return milisegundos

if __name__ == '__main__':
    print(solucion(dias=1, horas=1, minutos=1, segundos=1))