from datetime import datetime
# * Reto #15
# * ¿CUÁNTOS DÍAS?
# * Fecha publicación enunciado: 11/04/22
# * Fecha publicación resolución: 18/04/22
# * Dificultad: DIFÍCIL
# *
# * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# * - La función recibirá dos String y retornará un Int.
# * - La diferencia en días será absoluta (no importa el orden de las fechas).
# * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def main(fecha1 : str, fecha2 : str ):
    fecha1 : datetime = convertirFechas(fecha = fecha1)
    fecha2: datetime = convertirFechas(fecha = fecha2)

    diferencia = fecha2 - fecha1
    print(diferencia.days)

def convertirFechas(fecha: str)->datetime:
    fechaList: list[int] = fecha.split('/')
    print('Error la fecha esta incorrecta, favor de revisar')
    if len(fechaList) != 3:
        print('La fecha esta mal ordenada')
    else:
        fechaDate: datetime = datetime(int(fechaList[2]), int(fechaList[1]), int(fechaList[0]))
        return fechaDate

if __name__ == '__main__':
    main(fecha1='mouredev', fecha2='29/05/2022')
