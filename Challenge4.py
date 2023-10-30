 # * Reto #4
 # * ÁREA DE UN POLÍGONO
 # * Fecha publicación enunciado: 24/01/22
 # * Fecha publicación resolución: 31/01/22
 # * Dificultad: FÁCIL
 # *
 # * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 # * - La función recibirá por parámetro sólo UN polígono a la vez.
 # * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 # * - Imprime el cálculo del área de un polígono de cada tipo.
 # *
 # * Información adicional:
 # * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 # * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.



def main(poligono: str, base: int,  altura: int  ):

    match poligono:
        case 'trinangulo':
            resultado: float = trinangulo(base=base, altura=altura)
            print(resultado)
        case "cuadrado":
            resultado: float = cuadrado(lado=base)
            print(resultado)
        case 'rectangulo':
            resultado : float = rectangulo(longitud=base, anchura=altura)
            print(resultado)
        case _:
            print('Te equivocaste al escribir la figura geometrica')

def trinangulo(base: float, altura: float) -> float: return (base * altura) / 2
def cuadrado(lado: float) -> float: return lado * lado
def rectangulo(longitud: float, anchura: float) -> float: return longitud * anchura

if __name__ == '__main__':
    main(poligono='trinangulo', base= 5, altura=10 )

#
# class Polygon:
#     def area(self):
#         pass
#
#     def print_area(self):
#         pass
#
#
# class Triangle(Polygon):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return (self.base * self.height) / 2
#
#     def print_area(self):
#         print(f'El área del triángulo es {self.area()}')
#
#
# class Rectangle(Polygon):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def print_area(self):
#         print(f'El área del rectángulo es {self.area()}')
#
#
# class Square(Polygon):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
#
#     def print_area(self):
#         print(f'El área del cuadrado es {self.area()}')
#
#
# def area(polygon):
#     polygon.print_area()
#     return polygon.area()
#
#
# def main():
#     area(Triangle(10.0, 5.0))
#     area(Rectangle(5.0, 7.0))
#     area(Square(4.0))
#
#
# if __name__ == "__main__":
#     main()
#
