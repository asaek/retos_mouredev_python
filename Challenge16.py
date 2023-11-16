# * Reto #16
# * EN MAYÚSCULA
# * Fecha publicación enunciado: 18/04/22
# * Fecha publicación resolución: 25/04/22
# * Dificultad: FÁCIL
# *
# * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
# * poner en mayúscula la primera letra de cada palabra.
# * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def mayusculasString(oracion: str)-> str:
    listPalabras: list[str] = oracion.split(' ')
    listMayusPalabras: list[str] = []
    for palabra in listPalabras:
        listpalabra: list[str] = list(palabra)
        # print(listpalabra)
        for i in range(0, len(listpalabra)):
            if listpalabra[i].isalpha():
                listpalabra.insert(i, listpalabra[i].upper())
                del (listpalabra[i + 1])
                # print(listpalabra)
                listMayusPalabras.append(''.join(listpalabra))
                break
    oracion: str = ' '.join(listMayusPalabras)
    return oracion

if __name__ == '__main__':
    print(mayusculasString(oracion="¿hola qué tal estás?"))