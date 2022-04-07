import math


class Punto:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY

    def mover(self, increaseX, increaseY):
        self.coordX = increaseX
        self.coordY = increaseY

    def calcularDistancia(self, puntoExterno):
        return math.sqrt( (puntoExterno.coordX - self.coordX)**2 + (puntoExterno.coordY - self.coordY)**2 )