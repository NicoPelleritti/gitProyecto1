"""import re

# Exprecion regular
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
#print(re.findall('LV?Q?-[A-Z]{3}\s',matriculas))        #en ves de \s se puede usar $ en ambos casos
#print(re.findall('LV-[X|S]X?\d{3}\s',matriculas))


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
#print(re.findall('^([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|1[0-8][0-9][0-9]|1900)$',cadena))

cadena_numeros = input("Ingrese un numero natural para chequear si es menor a 1900: \n")
if (re.findall('^([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|1[0-8][0-9][0-9])$',cadena_numeros)):
        print("Es menor a 1900")
else:
    print("No es menor a 1900")
"""

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


#Recursion 2

def lista(lista_de_listas):
    if len(lista_de_listas) == 1:
        return lista_de_listas[0]
    else:
        return lista_de_listas[0] + lista(lista_de_listas[1:])

L = [[1,2,3],[4,5,6],[7],[8]]
print(lista(L))


#Recursion 3

def listas_iguales(L1,L2):
    if (len(L1) == len(L2) and len(L1) == 1):
        return L1[0]
    elif (len(L1) != len(L2)):
       return False
    else:
        if (L1[0] == L2[0] and listas_iguales(L1[1:],L2[1:])):
            return True
        else:
            return False

L1 = [1,2,3,4,6,2,3]
L2 = [2,1,3,4,6,2,3]

print(listas_iguales(L1,L2))


#Recursion 4

def division_entera(a,b):
    if b > a:
        return False
    elif (b <= a):
        return int(a/b)
    else:
        return division_entera(a,b)

print(division_entera(7,3))
print(division_entera(16,2))
print(division_entera(5,6))
