# Definiendo la clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__edad = edad

    # Método público para obtener información del animal
    def obtener_informacion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

    # Método público para obtener el nombre del animal
    def obtener_nombre(self):
        return self.__nombre

    # Método público para obtener la edad del animal
    def obtener_edad(self):
        return self.__edad

    # Método para hacer un sonido genérico (será sobrescrito en las clases derivadas)
    def hacer_sonido(self):
        return "Algún sonido genérico"


# Definiendo la clase derivada Perro, que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        # Atributo privado adicional (encapsulación)
        self.__raza = raza

    # Sobrescribiendo el método hacer_sonido para demostrar polimorfismo
    def hacer_sonido(self):
        return "Guau"

    # Método público para obtener la raza del perro
    def obtener_raza(self):
        return self.__raza

    # Sobrescribiendo el método obtener_informacion para incluir la raza del perro
    def obtener_informacion(self):
        return f"Nombre: {self.obtener_nombre()}, Edad: {self.obtener_edad()}, Raza: {self.__raza}"


# Definiendo la clase derivada Gato, que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        # Atributo privado adicional (encapsulación)
        self.__color = color

    # Sobrescribiendo el método hacer_sonido para demostrar polimorfismo
    def hacer_sonido(self):
        return "Miau"

    # Método público para obtener el color del gato
    def obtener_color(self):
        return self.__color

    # Sobrescribiendo el método obtener_informacion para incluir el color del gato
    def obtener_informacion(self):
        return f"Nombre: {self.obtener_nombre()}, Edad: {self.obtener_edad()}, Color: {self.__color}"


# Función principal para demostrar la funcionalidad del programa
def main():
    # Crear instancias de Perro y Gato
    mi_perro = Perro("Buddy", 5, "Golden Retriever")
    mi_gato = Gato("Whiskers", 3, "Gris")

    # Demostrar encapsulación y obtener información
    print(mi_perro.obtener_informacion())  # Debería imprimir: Nombre: Buddy, Edad: 5, Raza: Golden Retriever
    print(mi_gato.obtener_informacion())   # Debería imprimir: Nombre: Whiskers, Edad: 3, Color: Gris

    # Demostrar polimorfismo
    animales = [mi_perro, mi_gato]
    for animal in animales:
        print(f"{animal.obtener_nombre()} dice: {animal.hacer_sonido()}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()