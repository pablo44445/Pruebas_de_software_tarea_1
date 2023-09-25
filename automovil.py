from util import Util

class Automovil:
    def __init__(self, ID, Marca, Anio, Color, Precio, Turbo, Tipo, Motor, Cabinas, Sunroof):
        """
        Inicializa un objeto Automovil con los atributos especificados.

        Args:
            ID (int): ID único del automóvil.
            Marca (str): Marca del automóvil.
            Anio (int): Año del automóvil.
            Color (str): Color del automóvil.
            Precio (int): Precio del automóvil.
            Turbo (str): Si tiene turbo o no.
            Tipo (str): Tipo de automóvil (Sedan, Camioneta, SUV).
            Motor (str): Motor del automóvil.
            Cabinas (int): Cantidad de cabinas (Solo para Camionetas).
            Sunroof (str): Si tiene sunroof (Solo para SUV).
        """
        self.ID = ID
        self.Marca = Marca
        self.Anio = Anio
        self.Color = Color
        self.Precio = Precio
        self.Turbo = Turbo
        self.Tipo = Tipo
        self.Motor = Motor
        self.Cabinas = Cabinas
        self.Sunroof = Sunroof
        self.Popularidad = 0

    def contactar_agencia(self):
        """
        Incrementa la popularidad del automóvil cuando se contacta con la agencia.
        """
        self.Popularidad += 1

    def obtener_informacion(self):
        """
        Devuelve la información del automóvil como una cadena de texto.

        Returns:
            str: Información del automóvil.
        """
        return f"ID: {self.ID}\nMarca: {self.Marca}\nAño: {self.Anio}\nColor: {self.Color}\nPrecio: {self.Precio}\nTurbo: {self.Turbo}\nTipo: {self.Tipo}\nMotor: {self.Motor}\nCabinas: {self.Cabinas}\nSunroof: {self.Sunroof}\nPopularidad: {self.Popularidad}"

    def __str__(self):
        return self.obtener_informacion()
