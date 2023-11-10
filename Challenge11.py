# * Reto #11
# * ELIMINANDO CARACTERES
# * Fecha publicación enunciado: 14/03/22
# * Fecha publicación resolución: 21/03/22
# * Dificultad: FÁCIL
# *
# * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.


def main(string1: str, string2: str):
    string1Limpia: str = string1.lower().replace(' ' , '')
    string2Limpia: str = string2.lower().replace(' ' , '')
    string1Recortada: str = string1.lower().replace(' ' , '')
    string2Recortada: str = string2.lower().replace(' ' , '')

    for letra in string1Limpia:
        string2Recortada = string2Recortada.replace(letra, '')

    for letra in string2Limpia:
        string1Recortada = string1Recortada.replace(letra, '')
    print(string1Recortada)
    print(string2Recortada)

if __name__ == '__main__':
    main(string1='brais', string2='moure')
