# Ejercicio 5: Herencia Multinivel y Sobrescritura de Métodos
class Animal:
    def HacerSonido(self):
        print("El animal hace un sonido.")


class Mamifero(Animal):
    def Alimentar(self):
        print("El mamífero está siendo alimentado.")


class Perro(Mamifero):
    def HacerSonido(self):
        print("El perro dice: ¡Guau!")


# --- Pruebas de funcionamiento ---
if __name__ == "__main__":
    mi_perro = Perro()

    # Método heredado de Mamifero
    mi_perro.Alimentar()

    # Método sobrescrito en Perro
    mi_perro.HacerSonido()

    # Referencia de tipo Animal apuntando a un objeto Perro
    animal: Animal = mi_perro

    print("\nLlamada mediante una referencia de tipo Animal:")
    animal.HacerSonido()
