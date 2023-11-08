# * Reto #10
# * EXPRESIONES EQUILIBRADAS
# * Fecha publicación enunciado: 07/03/22
# * Fecha publicación resolución: 14/03/22
# * Dificultad: MEDIA
# *
# * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def main(cadena: str):
    # listaApertura: list[str] = ['{', '[', '(']
    # listaCerradura: list[str] = ['}',']',')']
    cadenaLimpia: str = cadena.replace(' ', '')
    listaAbiertos: list[str] = []
    listAbiPos: list[int] = []

    listaCerrados: list[str] = []
    listCerraPos: list[int] = []
    for i in range(0, len(cadenaLimpia)):
        match cadenaLimpia[i]:
            case '{':
                listaAbiertos.insert(0, '}')
                listAbiPos.insert(0, i)
            case '[':
                listaAbiertos.insert(0, ']')
                listAbiPos.insert(0, i)
            case '(':
                listaAbiertos.insert(0, ')')
                listAbiPos.insert(0, i)
            # Corchetes que cierran
            case '}':
                listaCerrados.append(cadenaLimpia[i])
                listCerraPos.append(i)
            case ']':
                listaCerrados.append(cadenaLimpia[i])
                listCerraPos.append(i)
            case ')':
                listaCerrados.append(cadenaLimpia[i])
                listCerraPos.append(i)

    print(f'{listaAbiertos} Post{listAbiPos} -- {listaCerrados} Post{listCerraPos}')

    if len(listaAbiertos) != len(listaCerrados):
        print('Error la exprecion no esta balanceada')
        return
    for i in range(0, len(listaAbiertos)):
        if listaAbiertos[i] != listaCerrados[i] or listAbiPos[i] > listCerraPos[i]:
            print('Error la exprecion no esta balanceada')
            return

    print("Esta Balanceada la exprecion y correcta :) ")
    return


if __name__ == '__main__':
    # main(cadena='{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }')
    main(cadena='{[a * (c + d)] - 5}')
    # main(cadena='{ a * ( c + d ) ] - 5 }')
    # main(cadena='(a')
    # main(cadena='{{{{{{(}}}}}}')
    # main(cadena='{a^4 + (((ax4)}')