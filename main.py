import re
import functools
from functools import reduce

def uno():
    # Expresion regular
    # 1
    matriculas = '''
    LV-QWE
    LQ-ABC
    LQ-ABT
    LV-X443
    LV-S586
    LV-SX334
    LA-123
    LX-ABC
    LV
    LV-344
    '''

    palabra = input("Ingrese la matricula a chequear: ")
    if (re.findall('\b(LV|LQ)-(S|SX|X)+(\d{3})',palabra) or re.findall('^(LV|LQ)+-[A-Z]{3}',palabra)):
        print("Cumple con la condicion")
    else:
        print("No cumple con la condicion")

    # 2
    cadena = '''
    2000
    6900
    1900
    1950
    3000
    1056
    300
    035
    637
    12
    1
    '''

    cadena_numeros = input("Ingrese un numero natural para chequear si es menor a 1900: \n")
    if (re.findall('^([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|1[0-8][0-9][0-9])$',cadena_numeros)):
            print("Es menor a 1900")
    else:
        print("No es menor a 1900")

def dos():
    #Recursion 1

    def conversor(num):
        if len(num) == 1:
            if num[0] % 2 == 0:
                return "1"
            else:
                return "2"
        else:
            if num[0] % 2 == 0:
                return "1" + conversor(num[1:])
            else:
                return "2" + conversor(num[1:])

    cadena = input("Ingrese un numero entero: \n")
    cadena = [int(x) for x in str(cadena)]
    print(conversor(cadena))

    # Recursion 2

    def lista(lista_de_listas):
        if len(lista_de_listas) == 1:
            return lista_de_listas[0]
        else:
            return lista_de_listas[0] + lista(lista_de_listas[1:])

    L = [[1, 2, 3], [4, 5, 6], [7], [8]]
    print(lista(L))

    # Recursion 3

    def listas_iguales(L1, L2):
        if (len(L1) == len(L2) and len(L1) == 1):
            return L1[0]
        elif (len(L1) != len(L2)):
            return False
        else:
            if (L1[0] == L2[0] and listas_iguales(L1[1:], L2[1:])):
                return True
            else:
                return False

    L1 = [1, 2, 3, 4, 6, 2, 3]
    L2 = [2, 1, 3, 4, 6, 2, 3]

    print(listas_iguales(L1, L2))

    # Recursion 4

    def division_entera(a, b):
        if b > a:
            return False
        elif (b <= a):
            return int(a / b)
        else:
            return division_entera(a, b)

    print(division_entera(7, 3))
    print(division_entera(16, 2))
    print(division_entera(5, 6))


def tres():
    #Colecciones 2
    num = int(input("Ingrese un numero para generar la sumatoria en pi: \n"))
    lista = []
    #Hacemos la lista decreciente para usar en el map
    def crearListaDecreciente(num, lista):
        if num == 0:
            return lista.append(0)
        else:
           lista.append(num)
           crearListaDecreciente(num - 1, lista)
           return lista

    print(crearListaDecreciente(num,lista))


    def sumatoriaPi(num):
        return 4*(-1)**num/(2*num+1)


    suma = list(map(sumatoriaPi,lista))
    print(suma)
    resultado = reduce(lambda a,b: a+b, suma)

    print(resultado)

def cuatro():
    #XML
    import xml.etree.ElementTree as ET
    doc_xml = '''
    <estaciones>
        <estacion latitud ="10" longitud ="5" nombre="a5b3">
            <sensores cantidad ="5">
                <humedad>1000hpa</humedad>
                <direccionviento>Norte</direccionviento>
                <velocviento>40km/h</velocviento>
                <temperatura>100°F</temperatura>
                <presion>50Pa</presion>
            </sensores>
        </estacion>
        <estacion latitud ="5" longitud ="7" nombre="z8v9">
            <sensores cantidad="2">
                <temperatura>23°C</temperatura>
                <presion>74Pa</presion>
            </sensores>
        </estacion>
        <estacion latitud ="100" longitud ="59" nombre="h4g2">
            <sensores cantidad="1">
                <direccionviento>Sur</direccionviento>
            </sensores>
        </estacion>
    </estaciones>
    '''

    #Json
    import json
    doc_json = '''
    {
     "estacion 1" : {
        "voltaje" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        "latitud" : "10",
        "longitud" : "5",
        "nombre" : "a5b3",
        "sensores" : {
            "Humedad" : {
            "valor" : "1000",
            "medida" : "hpa"
            },
            "Direccion viento" : {
            "valor" : "Norte",
            "medida" : " "
            },
            "Veloc viento" : {
            "valor" : "40",
            "medida" : "K/h"
            },
            "Temperatura" : {
            "valor" : "100",
            "medida" : "°F"
            },
            "Presion" : {
            "valor" : "50",
            "medida" : "Pa"
            }
       }
     },
     "estacion 2" : {
        "voltaje" : [1,2,3,4,5,6,7,8,9,80,11,11,13,14,33,30,75,81,30,25],
        "latitud" : "5",
        "longitud" : "7",
        "nombre" : "z8v9",
        "sensores" : {
            "Temperatura" : {
            "valor" : "23",
            "medida" : "°C"        
            },
            "Presion" : {
            "valor" : "74",
            "medida" : "Pa"        
            }
       } 
     } ,
     "estacion 3" : {
        "voltaje" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        "latitud" : "100",
        "longitud" : "59",
        "nombre" : "h4g2",
        "sensores" : {
            "Direccion viento" : {
            "valor" : "Sur",
            "medida" : " "
            }
       }
     }
    }
    '''

    d = json.loads(doc_json)
    cant_sens = 0

    for dicc in d:
    #    print(d[dicc])
        for sen in d[dicc]["sensores"]:
            cant_sens += 1
        print("\nCantidad de sensores de la estacion {}: {}".format(dicc, cant_sens))
        cant_sens = 0
        for sen in d[dicc]["sensores"]:
            print("{} : {} {}".format(sen,d[dicc]["sensores"][sen]["valor"],d[dicc]["sensores"][sen]["medida"]))

    volt_total = 0
    promedio = {}
    for dicc in d:
        for volt in d[dicc]["voltaje"]:
            volt_total += volt
        promedio[dicc] = (volt_total/20)
        volt_total = 0

    menor = promedio[dicc]
    estacion = ""
    for clave, valor in promedio.items():
        if valor <= menor:
            menor = valor
            estacion = clave
    print("el valor menor es: {}, de la estacion {}".format(menor,estacion))

opcion = int(input("Seleccione la opcion que de sea ejecutar: \n1:Expresion regular \n2:Recursión \n3:Colecciones \n4:XML/JSON \n5:Salir \n"))
while(opcion != 5):
    if opcion == 1:
        uno()
    if opcion == 2:
        dos()
    if opcion == 3:
        tres()
    if opcion == 4:
        cuatro()
    opcion = int(input("Seleccione la opcion que de sea ejecutar: \n1:Expresion regular \n2:Recursión \n3:Colecciones \n4:XML/JSON \n5:Salir \n"))
exit()