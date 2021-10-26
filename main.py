import re

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
