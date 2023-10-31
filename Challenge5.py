 # * Reto #5
 # * ASPECT RATIO DE UNA IMAGEN
 # * Fecha publicación enunciado: 01/02/22
 # * Fecha publicación resolución: 07/02/22
 # * Dificultad: DIFÍCIL
 # *
 # * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 # * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
 # * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 # * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 # *
 # * Información adicional:
 # * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 # * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

import requests
from PIL import Image

url_imagen = 'https://japannews.yomiuri.co.jp/wp-content/uploads/2023/07/10618521.jpg'
nombre_archivo = 'imagen_descargada.png'

def descargar_imagen(url: str, nombre_archivo: str):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:  # Verifica que la petición fue exitosa
        # si no existe el archivo lo creara para sustituirlo
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
            print(f'Imagen guardada como {nombre_archivo}')
    else:
        print(f'No se pudo descargar la imagen: {respuesta.status_code}')

def obtener_resolucion(nombre_archivo: str) -> tuple:
    with Image.open(nombre_archivo) as imagen:
        return imagen.size

def comunDenominador(width: int, height: int) -> int:
    while(height != 0):
        t: int = height
        height = width % height
        width = t
    return width

def obtenerRelacionAspecto( width: int, height: int )-> str:
    divisor: int = comunDenominador(width= width, height=height)
    return f'{width // divisor} : {height // divisor}'


def main():
    descargar_imagen(url=url_imagen, nombre_archivo=nombre_archivo)
    resolucion: tuple = obtener_resolucion(nombre_archivo=nombre_archivo)
    print(resolucion)
    print(obtenerRelacionAspecto(width=resolucion[0],height=resolucion[1]))

if __name__ == '__main__':
    main()