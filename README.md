#Introducción#

La Programación Orientada a Objetos (POO) es un paradigma de programación que permite modelar problemas del mundo real mediante clases y objetos, facilitando la organización, reutilización y mantenimiento del código. En el presente trabajo se desarrolla un sistema básico de gestión de vehículos utilizando el lenguaje de programación Python, aplicando los principios fundamentales de la POO.

El objetivo principal de este programa es gestionar la información de distintos tipos de vehículos dentro de un taller, demostrando el uso de modularidad, herencia, polimorfismo y buenas prácticas de programación.

#Desarrollo#

El sistema fue desarrollado en Python aplicando el paradigma de la Programación Orientada a Objetos, con el fin de modelar un escenario del mundo real: la gestión de vehículos en un taller. Para ello, el programa se estructuró de forma modular, separando las responsabilidades en distintos módulos, lo que mejora la organización, la comprensión del código y su mantenimiento.

Las clases se utilizan como base del diseño del sistema. La clase Vehículo representa un vehículo genérico y contiene atributos como marca, modelo, año y disponibilidad. A partir de esta clase se crean objetos que representan vehículos reales, evidenciando el uso de objetos como instancias de una clase.

El encapsulamiento se aplica al agrupar los datos y comportamientos dentro de cada clase. Los atributos de los vehículos se gestionan internamente mediante métodos, evitando manipulaciones directas desde otras partes del programa y manteniendo un control adecuado de la información.

La herencia se implementa mediante la clase VehículoEléctrico, la cual hereda de la clase Vehículo. Esta clase reutiliza los atributos y métodos de la clase base y añade una característica específica: el nivel de batería. Esto permite extender la funcionalidad sin duplicar código, cumpliendo uno de los principios fundamentales de la POO.

El polimorfismo se evidencia al mostrar la información de los vehículos. Aunque todos los vehículos son tratados de la misma manera dentro del sistema, cada tipo presenta su información de forma distinta, dependiendo de si es un vehículo convencional o eléctrico, demostrando comportamientos diferentes para un mismo método.

Además, el programa hace uso correcto de distintos tipos de datos, como cadenas de texto para marca y modelo, números enteros para el año, valores booleanos para la disponibilidad y números decimales para la batería. También se aplican buenas prácticas de programación, como el uso de nombres descriptivos en snake_case, comentarios claros y un punto de entrada principal que permite ejecutar correctamente el sistema.

#Conclusión#

En conclusión, el sistema de gestión de vehículos desarrollado cumple correctamente con los requisitos planteados, aplicando de manera adecuada los principios de la Programación Orientada a Objetos. La utilización de clases, herencia y polimorfismo permitió modelar un problema del mundo real de forma clara y eficiente.

Además, la modularidad del proyecto facilita su comprensión y posible ampliación futura. Este trabajo demuestra la importancia de la POO en el desarrollo de aplicaciones estructuradas y mantenibles, así como el correcto uso de Python como herramienta para la solución de problemas informáticos.
