class CuentaBancaria:

    def __init__(self, numero_cuenta: str,propietario: str,):
        self.numero_cuenta: str = numero_cuenta
        self.propietrario: str = propietario
        self.balance: float = 0

    def depositar(self, cantidad: float):
        self.balance += cantidad

    def retirar(self, cantidad: float):
        self.balance -= cantidad

if __name__ == "__main__":
    cuenta_1: CuentaBancaria = CuentaBancaria("9283749","Carlos")
    cuenta_2: CuentaBancaria = CuentaBancaria("9200029", "Juan")
    cuenta_3: CuentaBancaria = CuentaBancaria("0998777", "Mario")

    cuenta_1.depositar(20000)


    print(cuenta_1.balance)