"""
Archivo: vehiculo_electrico.py
Descripción:
Este módulo define la clase VehiculoElectrico, que hereda de Vehiculo.
Aplica herencia y polimorfismo.
"""

from .Vehiculo import Vehiculo

class VehiculoElectrico(Vehiculo):
    """
    Clase que representa un vehículo eléctrico.
    Hereda atributos y métodos de la clase Vehiculo.
    """

    def __init__(self, marca, modelo, anio, disponible, capacidad_bateria):
        """
        Constructor de la clase VehiculoElectrico.

        :param marca: Marca del vehículo (str)
        :param modelo: Modelo del vehículo (str)
        :param anio: Año de fabricación (int)
        :param disponible: Estado de disponibilidad (bool)
        :param capacidad_bateria: Capacidad de la batería en kWh (int)
        """
        super().__init__(marca, modelo, anio, disponible)
        self.capacidad_bateria = capacidad_bateria

    def __str__(self):
        """
        Retorna una representación en texto del vehículo eléctrico.
        """
        return super().__str__() + f" - Batería: {self.capacidad_bateria} kWh"
