# * Reto #9
# * CÓDIGO MORSE
# * Fecha publicación enunciado: 02/03/22
# * Fecha publicación resolución: 07/03/22
# * Dificultad: MEDIA
# *
# * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
diccCodigoMorse: dict[str, str] = {
    'a': '._', 'b': '_...','c': '_._.','d': '_..','e': '.','f': '.._.','g': '__.','h': '....','i': '..',
    'j': '.___','k': '_._','l': '._..','m': '__','n': '_.','o': '___','p': '.__.','q': '__._','r': '._.','s': '....',
    't': '_','u': '.._','v': '..._','w': '.__','x': '_.._','y': '_.__','z': '__..',
    '1': '.___','2': '..___','3': '...__','4': '...._','5': '.....','6': '_....','7': '__...','8': '___..','9': '____.','0': '_____',
}

def main(mensaje: str):
    codigoMorse: str = ""
    # print(mensaje.lower().replace(" ",""))
    for caracter in mensaje.lower().replace(" ",""):
        # print(caracter)
        if caracter in diccCodigoMorse:
            codigoMorse += diccCodigoMorse[caracter]
            # print(f'{diccCodigoMorse[caracter]}')
    print(codigoMorse)

if __name__ == '__main__':
    main(mensaje='A s a')