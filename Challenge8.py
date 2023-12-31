 # * DECIMAL A BINARIO
 # * Fecha publicación enunciado: 18/02/22
 # * Fecha publicación resolución: 02/03/22
 # * Dificultad: FÁCIL
 # *
 # * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 # *
 # * Información adicional:
 # * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 # * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def main(numero: int):
    # numeroBinario: list[int] = []
    binario: str = ''
    while numero != 0:
        # binario: int = numero % 2
        # numeroBinario.insert(0, binario)
        binario = str(numero % 2) + binario
        numero = numero // 2
    print(int(binario))

if __name__ == '__main__':
    main(numero=50)