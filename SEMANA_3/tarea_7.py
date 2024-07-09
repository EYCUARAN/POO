class ManejadorDeArchivos:
    def __init__(self, nombre_archivo, modo):
        """
        Constructor que inicializa el objeto ManejadorDeArchivos.

        :param nombre_archivo: Nombre del archivo a abrir.
        :param modo: Modo en el que se abrirá el archivo (por ejemplo, 'r' para leer, 'w' para escribir).
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
        try:
            self.archivo = open(nombre_archivo, modo)
            print(f"Archivo '{nombre_archivo}' abierto en modo '{modo}'.")
        except IOError as e:
            print(f"No se pudo abrir el archivo: {e}")

    def escribir_datos(self, datos):
        """
        Escribe datos en el archivo si está abierto en modo escritura.

        :param datos: Datos a escribir en el archivo.
        """
        if self.archivo and 'w' in self.modo:
            self.archivo.write(datos)
            print(f"Datos escritos en el archivo '{self.nombre_archivo}'.")
        else:
            print("El archivo no está abierto en modo escritura.")

    def leer_datos(self):
        """
        Lee datos del archivo si está abierto en modo lectura.

        :return: Datos leídos del archivo.
        """
        if self.archivo and 'r' in self.modo:
            datos = self.archivo.read()
            print(f"Datos leídos del archivo '{self.nombre_archivo}'.")
            return datos
        else:
            print("El archivo no está abierto en modo lectura.")
            return None

    def __del__(self):
        """
        Destructor que cierra el archivo si está abierto y realiza la limpieza.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado.")

# Uso de la clase ManejadorDeArchivos
def main():
    # Crear un objeto ManejadorDeArchivos para escribir datos en un archivo
    escritor = ManejadorDeArchivos('ejemplo.txt', 'w')
    escritor.escribir_datos('Hola, este es un ejemplo de uso de constructores y destructores en Python.\n')

    # Crear un objeto ManejadorDeArchivos para leer datos de un archivo
    lector = ManejadorDeArchivos('ejemplo.txt', 'r')
    contenido = lector.leer_datos()
    if contenido:
        print("Contenido del archivo:\n" + contenido)

if __name__ == "__main__":
    main()