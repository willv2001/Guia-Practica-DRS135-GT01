# Ejercicio 2: Empleado
class Empleado:
    def __init__(self, nombre, edad):
        # Atributo privado para cumplir con la encapsulación
        self.__nombre = nombre
        
        # Valor de respaldo por si falla la validación al instanciar
        self.__edad = 0 
        
        # Paso el valor por el setter para obligar a que se valide desde el inicio
        self.edad = edad  

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        # Verificamos que la edad tenga sentido lógico
        if valor > 0 and valor < 100:
            self.__edad = valor
        else:
            # Lanzo un error para evitar que el objeto guarde datos inválidos
            raise ValueError("La edad debe estar entre 1 y 99 años.")

# --- Pruebas de funcionamiento ---
try:
    # Instancia con datos correctos
    empleado = Empleado("Carlos", 30)
    print(f"Empleado registrado: {empleado.nombre}, Edad: {empleado.edad}")

    # Actualización válida
    empleado.edad = 31
    print(f"Edad actualizada a: {empleado.edad}")

    # Forzamos un error para probar el candado de validación
    print("\nIntentando asignar 105 años...")
    empleado.edad = 105

except ValueError as e:
    # Atrapamos el error para que el programa no colapse
    print(f"Acción bloqueada: {e}")