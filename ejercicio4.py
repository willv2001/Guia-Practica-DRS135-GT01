# Ejercicio 4: Polimorfismo
class Animal:
    def HacerSonido(self):
        # Método base que será sobrescrito por las clases derivadas
        print("El animal hace un sonido.")


class Perro(Animal):
    def HacerSonido(self):
        print("El perro dice: ¡Guau!")


class Gato(Animal):
    def HacerSonido(self):
        print("El gato dice: ¡Miau!")


# --- Pruebas de funcionamiento ---
if __name__ == "__main__":
    animal1: Animal = Perro()
    animal2: Animal = Gato()

    animal1.HacerSonido()
    animal2.HacerSonido()

    print("\nRecorriendo la lista de animales:")
    animales: list[Animal] = [animal1, animal2]

    for animal in animales:
        animal.HacerSonido()
