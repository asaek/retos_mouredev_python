import re
# * Reto  # 12
# * ¿ES UN PALÍNDROMO?
# * Fecha publicación enunciado: 2 1 /0 3 /22
# * Fecha publicación resolución: 2 8 /0 3 /22
# * Dificultad: MEDIA
# *
# * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# * Ejemplo: Ana lleva al oso la avellana.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https :/ /mouredev.co m /discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def main(cadena: str):
    limpiaCadena: str = cadena.lower()
    limpiaCadena = re.sub(r"[.,:; ]", '',limpiaCadena)
    cadenaInvertida: str = limpiaCadena[::-1]
    print(cadenaInvertida)
    print(limpiaCadena)
    if cadenaInvertida == limpiaCadena:
        print("la cadena es palindromos")
    else:
        print('Error la cadena no es palindromos')

if __name__ == '__main__':
    main(cadena='.,Asaek.')