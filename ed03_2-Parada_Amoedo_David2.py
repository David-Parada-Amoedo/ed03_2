import math
import logging
import sys

# Configuración del logging para escribir tanto en archivo como en consola
# Crear un formateador que usaremos para ambos handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configurar el logger
logger = logging.getLogger('CalculadoraCientifica')
logger.setLevel(logging.INFO)

# Handler para archivo
file_handler = logging.FileHandler('calculadora.log')
file_handler.setFormatter(formatter)

# Handler para consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Añadir ambos handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class CalculadoraCientifica:
    def __init__(self):
        logger.info("Iniciando calculadora científica")

    def validar_numeros(self, *args):
        """Valida que los argumentos sean números"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    f"Se esperaba un número, se recibió {type(num)}")
            # Operaciones básicas

    def sumar(self, a, b):
        """Suma dos números"""
        self.validar_numeros(a, b)
        logger.info(f"Sumando {a} + {b}")
        return a + b

    def restar(self, a, b):
        """Resta dos números"""
        self.validar_numeros(a, b)
        logger.info(f"Restando {a} - {b}")
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números"""
        self.validar_numeros(a, b)
        logger.info(f"Multiplicando {a} * {b}")
        return a * b

    def dividir(self, a, b):
        """Divide dos números"""
        self.validar_numeros(a, b)
        if b == 0:
            logger.error("Intento de división por cero")
            raise ValueError("No se puede dividir por cero")
        logger.info(f"Dividiendo {a} / {b}")
        return a / b

    # Operaciones avanzadas
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        self.validar_numeros(base, exponente)
        logger.info(f"Calculando {base} ^ {exponente}")
        return math.pow(base, exponente)

    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        self.validar_numeros(numero)
        if numero < 0:
            logger.error(
                f"Intento de calcular raíz cuadrada de número negativo: {numero}")
            raise ValueError(
                "No se puede calcular la raíz cuadrada de un número negativo")
        logger.info(f"Calculando raíz cuadrada de {numero}")
        return math.sqrt(numero)

    def logaritmo_natural(self, numero):
        """Calcula el logaritmo natural de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error(
                f"Intento de calcular logaritmo de número no positivo: {numero}")
            raise ValueError(
                "No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info(f"Calculando logaritmo natural de {numero}")
        return math.log(numero)

    def logaritmo_base_10(self, numero):
        """Calcula el logaritmo en base 10 de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error(
                f"Intento de calcular logaritmo base 10 de número no positivo: {numero}")
            raise ValueError(
                "No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info(f"Calculando logaritmo base 10 de {numero}")
        return math.log10(numero)

    def seno(self, angulo):
        """Calcula el seno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info(f"Calculando seno de {angulo} radianes")
        return math.sin(angulo)

    def coseno(self, angulo):
        """Calcula el coseno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info(f"Calculando coseno de {angulo} radianes")
        return math.cos(angulo)

    def tangente(self, angulo):
        """Calcula la tangente de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info(f"Calculando tangente de {angulo} radianes")
        return math.tan(angulo)


def main():
    global sum1, sum2, rest1, rest2, mult1, mult2, div1, div2, pot1, pot2, raiz, logn, logb, angulo
    # Crear instancia de la calculadora
    sum1 = float(input("introduce el primer número para la suma: "))
    sum2 = float(input("introduce el segundo número para la suma: "))
    rest1 = float(input("introduce el primer número para la resta: "))
    rest2 = float(input("introduce el segundo número para la resta: "))
    mult1 = float(input("introduce el primer número para la multiplicación: "))
    mult2 = float(
        input("introduce el segundo número para la multiplicación: "))
    div1 = float(input("introduce el dividendo para la división: "))
    div2 = float(input("introduce el divisor para la división: "))
    pot1 = float(input("introduce base para calcular la potencia: "))
    pot2 = int(input("introduce el exponete de la potecia: "))
    raiz = float(input("introduce el número para calcular la raiz cuadrada: "))
    logn = float(input("introduce el número para su logaritmo natural: "))
    logb = float(input("introduce el número para el logaritmo en base 10: "))
    angulo = float(input("introduce el angulo para el cálculo: "))

    calc = CalculadoraCientifica()

    try:
        # Ejemplos de uso de operaciones básicas
        print("\n=== Operaciones Básicas ===")
        print(f"Suma de {sum1} + {sum2} = {calc.sumar(sum1, sum2)}")
        print(f"Resta de {rest1} - {rest2} = {calc.restar(rest1, rest2)}")
        print(
            f"Multiplicación de {mult1} * {mult2} = {calc.multiplicar(mult1, mult2)}")
        print(f"División de {div1} / {div2} = {calc.dividir(div1, div2)}")
        # Ejemplos de uso de operaciones avanzadas
        print("\n=== Operaciones Avanzadas ===")
        print(f"Potencia de {pot1}^{pot2} = {calc.potencia(pot1, pot2)}")
        print(f"Raíz cuadrada de {raiz} = {calc.raiz_cuadrada(raiz)}")
        print(f"Logaritmo natural de {logn} = {calc.logaritmo_natural(logn)}")
        print(f"Logaritmo base 10 de {logb} = {calc.logaritmo_base_10(logb)}")
        # Ejemplos de funciones trigonométricas
        print("\n=== Funciones Trigonométricas ===")
        # angulo = math.pi/2
        print(f"Seno de π/2 = {calc.seno(angulo)}")
        print(f"Coseno de π/2 = {calc.coseno(angulo)}")
        print(f"Tangente de π/4 = {calc.tangente(angulo)}")

        # Ejemplo de manejo de errores
        print("\n=== Prueba de Manejo de Errores ===")
        print("Intentando dividir por cero:")
        calc.dividir(5, 0)

    except ValueError as e:
        logger.error(f"Error de valor: {str(e)}")
        print(f"Error de valor: {e}")
    except TypeError as e:
        logger.error(f"Error de tipo: {str(e)}")
        print(f"Error de tipo: {e}")
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
