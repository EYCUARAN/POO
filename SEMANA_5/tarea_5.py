"""
Solicitar al usuario el nombre del estudiante (string).
Solicitar al usuario la edad del estudiante (integer).
Solicitar al usuario el sexo del estudiante (string, con opciones válidas).
Solicitar al usuario el promedio académico del estudiante (float).
Solicitar al usuario si el estudiante está activo en el sistema (boolean).
Muestra un resumen completo de la información del estudiante registrado.
"""


# Agregamos una funcion para registrar un nuevo estudiante
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante : ")  # Tipo de datos que va ingresar es caracter.
    edad = int(input("Ingrese la edad del estudiante : "))  # Tipo de dato que va ingresar es entero
    sexo = input("Ingrese el sexo del estudinate : ").upper()  # Tipo de datos que va ingresar es caracter.

    """Snake_case son nombres de variables y funciones
    que usan minúsculas y separan las palabras con guiones bajos (_). """

    while sexo not in ("M", "F"):
        sexo = input("Ingrese el sexo del estudiante M o F").upper()
    promedio = float(input("Ingrese el promedio academico del estudiante: "))  # Tipo de datos que va ingresar es float
    activo = input("El estudiante esta activo en el sistema S/N: ").upper()
    while activo not in ("S", "N"):
        activo = input("Respuesta  no validad. Ingrese S o N").upper()

    activo_bool = activo == "S"  # Tipo de datos que va ingresar es Booleano
    print(f" \n Resumen de estudiante : ")
    print(f"Nombre : {nombre}")  # Tipo de dato que se va imprimir es caracter
    print(f"Edad : {edad}")  # Tipo de dato que se va imprimir es Entero
    print(f"Sexo : {sexo}")  # Tipo de dato que se va imprimir es caracter
    print(f"Promedio de calificaciones: {promedio:.2f}")  # Tipo de dato que se va imprimir es Decimal
    print(f"Estudiante activo : {activo_bool}")  # Tipo de dato que se va imprimir es Booleono


registrar_estudiante()
