# Ejercicio 1: Cuenta Bancaria
class CuentaBancaria:
    def __init__(self):
        # Ocultamos el saldo desde el inicio para obligar a usar los métodos
        self.__saldo = 0.0

    def Depositar(self, monto):
        # Filtro para evitar ingresos negativos
        if monto > 0:
            self.__saldo += monto
        else:
            raise ValueError("El monto a depositar tiene que ser mayor a cero.")

    def Retirar(self, monto):
        # Doble validación: que el número sea válido y que alcance el dinero
        if monto <= 0:
            raise ValueError("No puedes retirar cantidades negativas o cero.")
        
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            raise ValueError("Saldo insuficiente para hacer este retiro.")

    def ObtenerSaldo(self):
        # Única vía permitida para ver el dinero (solo lectura)
        return self.__saldo

# --- Pruebas de funcionamiento ---
try:
    mi_cuenta = CuentaBancaria()
    
    # Probamos un flujo normal
    mi_cuenta.Depositar(150)
    print(f"Saldo después del depósito: ${mi_cuenta.ObtenerSaldo()}")
    
    mi_cuenta.Retirar(50)
    print(f"Saldo después del retiro: ${mi_cuenta.ObtenerSaldo()}")

    # Forzamos un error por falta de fondos para comprobar la seguridad
    print("\nIntentando retirar $200...")
    mi_cuenta.Retirar(200)

except ValueError as error:
    # Capturamos el error para demostrar que las validaciones bloquean la acción
    print(f"Operación rechazada: {error}")