"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar puntos de interconexión aérea")
    print("3- Encontrar clústeres de tráfico aéreo")
    print("4- Encontrar la ruta más corta entre ciudades")
    print("5- Utilizar las millas de viajero")
    print("6- Cuantificar el efecto de un aeropuerto cerrado")
    print("7- Comparar con servicio WEB externo - BONO")
    print("8- Visualizar gráficamente los requerimientos - BONO")
    print("0- Salir del menú")




def initCatalog():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()



def cargarData(catalog):
    """
    Carga la información en la estructura de datos
    """
    controller.cargarData(catalog)




def printReq1(result):
    
    return None


def printReq2(result):
    
    return None


def printReq3(result):
    
    return None


def printReq4(result):
    
    return None


def printReq5(result):
    
    return None


def printReq6(result):
    
    return None


def printReq7(result):
    
    return None















catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        cargarData(catalog)
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        result5 = None

    elif int(inputs[0]) == 2:
        result1 = controller.puntosInterconexionAerea(catalog)
        printReq1(result1)

    elif int(inputs[0]) == 3:
        iata1 = input("Ingrese el código IATA del primer aeropuerto: ")
        iata2 = input("Ingrese el código IATA del segundo aeropuerto: ")
        result2 = controller.clusteresTraficoAereo(catalog, iata1, iata2)
        printReq2(result2)

    elif int(inputs[0]) == 4:
        ciudad1 = input("Ingrese la ciudad de origen: ")
        ciudad2 = input("Ingrese la ciudad de destino: ")
        result3 = controller.rutaMasCorta(catalog, ciudad1, ciudad2)
        printReq3(result3)

    elif int(inputs[0]) == 5:
        ciudad = input("Ingrese la ciudad de origen: ")
        millas = input("Ingrese la cantidad de millas que tiene disponibles: ")
        result4 = controller.usarMillasViajero(catalog, ciudad, millas)
        printReq4(result4)

    elif int(inputs[0]) == 6:
        iata = input("Ingrese el código IATA del aeropuerto fuera de funcionamiento: ")
        result5 = controller.efectoAeropuertoCerrado(catalog, iata)
        printReq5(result5)

    elif int(inputs[0]) == 7:
        ciudad1 = input("Ingrese la ciudad de origen: ")
        ciudad2 = input("Ingrese la ciudad de destino: ")
        result6 = controller.compararWebExterno(catalog, ciudad1, ciudad2)
        printReq6(result6)

    elif int(inputs[0]) == 8:
        controller.graficarReq(result1, result2, result3, result4, result5)

    else:
        sys.exit(0)
sys.exit(0)
