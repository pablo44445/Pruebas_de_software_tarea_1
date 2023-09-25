import random

class Util:
    @staticmethod
    def generar_numero_aleatorio(minimo, maximo):
        """
        Genera un número entero aleatorio entre los valores especificados.

        Args:
            minimo (int): Valor mínimo.
            maximo (int): Valor máximo.

        Returns:
            int: Número aleatorio entre minimo y maximo.
        """
        return random.randint(minimo, maximo)
