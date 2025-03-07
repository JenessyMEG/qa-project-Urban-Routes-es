## Jenessy Esteves. Grupo 10. Sprint 8
# Proyecto Urban Routes in Pycharm
## Driver Urban Routes
Urban Routes es un servicio que crea rutas para varios tipos de transporte. Calcula el tiempo y el costo del viaje.
La interfaz posee los campos "Desde" y "Hasta" y hay botones de selección del modo de ruta ("Óptimo", "Flash" y
"Personal") y también de selección del tipo de transporte (Comfort, laboral, relajante, entre otros), que permite la seleccion de personal de algunas comodidades como mantas y helados.
El usuario introduce el punto de partida y el destino, y luego los pasos anteriormentes mencionados.

Este proyecto trata de la ejecución de pruebas para una solcitud de un taxi en la modalidad "Comfort" que cubren todo el proceso de seleccion, desde las direcciones hasta la busqueda de un conductor.

# Programas Instalados

- Las herramienta:

-Pycharm
-Git Bash
-Git Hub Destokp
-Selenium WebDriver

- Paquetes dentro del Pycharm:

-Pip Pytest
-Selenium's Framworks

- Lenguaje de programacio:

-Python

# Objetivos de los archivos
El proyecto consta de 3 archivos fundamentales
- README.md: Posee documentación y una descripción informativa sobre el proyecto y que se esta probando en él
- data.py: Archivo utilizado para el almacenamiento de las rutas y datos de comprobacion
- main.py: Archivo que posee las clases declaras, la primera clase "UrbanRoutesPage" con los localizdores del sitio web que posteriormente son usados para la declaracion de los metodos y estos a su vez, usado en las pruebas declaradas en la clase "TestUrbanRoutes"; tambien posee funciones especificas para la obtención de un codigo telefónico.

# Como ejecutar el proyecto en la terminal

pytest C:\Users\wseve\qa-project-Urban-Routes-es

# Informacion relevante de la automatizacion

Es importante recordar que el serividor utilizado posee un tiempo de duracion, el cual se debe renovar en la variable "urban_routes_url" nombrada en el archivo data.py

