# Ejercicio 3: Herencia Simple
class Vehiculo:
    def Arrancar(self):
        # Método disponible para cualquier clase que herede de Vehiculo
        print("El vehículo ha arrancado.")

    def Detener(self):
        # Método común para detener el vehículo
        print("El vehículo se ha detenido.")


class Coche(Vehiculo):
    def Conducir(self):
        # Funcionalidad propia de la clase derivada
        print("El coche está siendo conducido.")


# --- Pruebas de funcionamiento ---
if __name__ == "__main__":
    mi_coche = Coche()

    # El objeto Coche puede utilizar los métodos heredados de Vehiculo
    mi_coche.Arrancar()
    mi_coche.Conducir()
    mi_coche.Detener()
