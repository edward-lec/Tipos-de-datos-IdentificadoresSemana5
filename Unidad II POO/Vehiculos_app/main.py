"""
Archivo: main.py
Descripción:
Punto de entrada del sistema de gestión de vehículos.
Desde este archivo se ejecuta el programa principal,
utilizando las clases de los módulos modelos y servicios.
"""

from servicios.taller import Taller
from modelos.Vehiculo import Vehiculo
from modelos.Vehiculo_electrico import VehiculoElectrico

def main():
    """
    Función principal del sistema.
    Aquí se crean los objetos y se ejecuta la lógica general.
    """

    # Creación del taller
    taller = Taller("Taller Central")

    # Creación de vehículos con distintos tipos de datos
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, True)
    vehiculo2 = Vehiculo("Chevrolet", "Aveo", 2019, False)

    # Creación de un vehículo eléctrico (herencia)
    vehiculo3 = VehiculoElectrico("Tesla", "Model 3", 2023, True, 75)

    # Agregar los vehículos al taller
    taller.agregar_vehiculo(vehiculo1)
    taller.agregar_vehiculo(vehiculo2)
    taller.agregar_vehiculo(vehiculo3)

    # Mostrar la información de los vehículos
    print("Listado de vehículos en el taller:\n")
    taller.mostrar_vehiculos()

# Punto de entrada del programa
if __name__ == "__main__":
    main()



