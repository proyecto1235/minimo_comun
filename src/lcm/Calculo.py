class src:
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        if a == 0 or b == 0:
            return 0  # El MCM con 0 se puede considerar como 0
        return abs(a * b) // src.gcd(a, b)

if __name__ == "__main__":
    # Pedimos los números al usuario
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    # Calculamos el MCM
    resultado = src.lcm(num1, num2)

    # Mostramos el resultado
    print(f"El mínimo común múltiplo de {num1} y {num2} es: {resultado}")
