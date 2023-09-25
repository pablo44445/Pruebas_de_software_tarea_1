from automovil import Automovil
from util import Util
import random

class Agencia:
    def __init__(self):
        """
        Inicializa una instancia de la clase Agencia con una lista de automóviles.
        """
        self.automoviles = []

    def generar_automoviles(self, cantidad):
        """
        Genera automóviles aleatorios y los agrega a la lista de la agencia.

        Args:
            cantidad (int): Cantidad de automóviles a generar.
        """
        for _ in range(cantidad):
            ID = Util.generar_numero_aleatorio(1000, 9999)
            Marca = random.choice(["Toyota", "Ford", "Honda", "Chevrolet", "Volkswagen"])
            Anio = Util.generar_numero_aleatorio(2015, 2023)
            Color = random.choice(["Rojo", "Azul", "Negro", "Blanco", "Gris"])
            Precio = Util.generar_numero_aleatorio(8000000, 30000000)
            Turbo = random.choice(["Si", "No"])
            Tipo = random.choice(["Sedan", "Camioneta", "SUV"])
            Motor = self.generar_motor(Tipo)
            Cabinas = random.choice([1, 2]) if Tipo == "Camioneta" else None
            Sunroof = random.choice(["Si", "No"]) if Tipo == "SUV" else None
            automovil = Automovil(ID, Marca, Anio, Color, Precio, Turbo, Tipo, Motor, Cabinas, Sunroof)
            self.automoviles.append(automovil)
    def obtener_vehiculos_por_pagina(self, pagina, vehiculos_por_pagina):
        """
        Obtiene los vehículos a mostrar en la página especificada.

        Args:
            pagina (int): Número de página.
            vehiculos_por_pagina (int): Cantidad de vehículos por página.

        Returns:
            list: Lista de vehículos para mostrar en la página actual.
        """
        inicio = (pagina - 1) * vehiculos_por_pagina
        fin = inicio + vehiculos_por_pagina
        return self.automoviles[inicio:fin]
    
    def calcular_total_paginas(self, vehiculos_por_pagina):
        """
        Calcula el número total de páginas necesarias para mostrar todos los vehículos.

        Args:
            vehiculos_por_pagina (int): Cantidad de vehículos por página.

        Returns:
            int: Número total de páginas.
        """
        total_vehiculos = len(self.automoviles)
        return (total_vehiculos + vehiculos_por_pagina - 1) // vehiculos_por_pagina

    def generar_motor(self, tipo):
        """
        Genera un tipo de motor aleatorio según el tipo de automóvil.

        Args:
            tipo (str): Tipo de automóvil (Sedan, Camioneta, SUV).

        Returns:
            str: Tipo de motor generado.
        """
        if tipo == "Sedan":
            return random.choice(["1.4cc", "1.6cc", "2.0cc"])
        elif tipo == "Camioneta":
            return random.choice(["2.4cc", "3.0cc", "4.0cc"])
        elif tipo == "SUV":
            return random.choice(["1.8cc", "2.2cc", "2.8cc"])

    def filtrar_automoviles(self, precio=None, tipo=None, color=None):
        """
        Filtra los automóviles de la agencia según los criterios especificados.

        Args:
            precio (int, optional): Precio máximo para filtrar. Default None.
            tipo (str, optional): Tipo de automóvil para filtrar. Default None.
            color (str, optional): Color del automóvil para filtrar. Default None.

        Returns:
            list: Lista de automóviles filtrados.
        """
        resultado = []
        for automovil in self.automoviles:
            if (precio is None or automovil.Precio <= precio) and \
               (tipo is None or automovil.Tipo == tipo) and \
               (color is None or automovil.Color == color):
                resultado.append(automovil)
        return resultado
