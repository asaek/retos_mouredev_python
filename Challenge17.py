from enum import Enum

# * Reto #17
# * LA CARRERA DE OBSTÁCULOS
# * Fecha publicación enunciado: 25/04/22
# * Fecha publicación resolución: 02/05/22
# * Dificultad: MEDIA
# *
# * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
# * carrera de obstáculos.
# * - La función recibirá dos parámetros:
# *      - Un array que sólo puede contener String con las palabras "run" o "jump"
# *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# * - La función imprimirá cómo ha finalizado la carrera:
# *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
# *        variará el símbolo de esa parte de la pista.
# *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
# *      - Si hace "run" en "|" (valla), se variará la pista por "/".
# * - La función retornará un Boolean que indique si ha superado la carrera.
# * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

class AthleteState(Enum):
    RUN = '_'
    JUMP = '|'


def main(accionesHechas: list[AthleteState], carretera: str)-> bool:
    listObstaculos: list[AthleteState] = listCarrera(carretera)
    terminadaCarreda: bool = True
    if not listObstaculos:
        return False
    # else:
        # print(listObstaculos)
    for i in range(1, len(listObstaculos)):
        if accionesHechas[i] != listObstaculos[i]:
            terminadaCarreda = False
            if listObstaculos[i] == AthleteState.RUN:
                carretera = carretera[:i-1] + 'X' + carretera[i+1:]
            elif listObstaculos[i] == AthleteState.JUMP:
                carretera = carretera[:i - 1] + '/' + carretera[i + 1:]

    print(carretera)
    return terminadaCarreda

def listCarrera (carretera: str) -> list[AthleteState]:
    listAcciones: list[AthleteState] = []
    for accion in carretera:
        if accion == '_':
            listAcciones.append(AthleteState.RUN)
        elif  accion == '|':
            listAcciones.append(AthleteState.JUMP)
        else:
            print('La pista esta incorrecta')
            return []
    return listAcciones






if __name__ == '__main__':
    print(main(accionesHechas=[AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP], carretera='||?||'))