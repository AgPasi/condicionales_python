# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n')).lower()

texto_2 = str(input('Ingrese la segunda palabra:\n')).lower()
print()

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

s = len(texto_1)
a = len(texto_2)

if s > a:
    print("Texto 1 es mayor que texto 2 ")

elif s < a:
    print("Texto 2 es mayor: que texto 1:")
elif texto_1[0] == texto_2[0]:
    print("Primeras letras iguales")


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if s > a:
    print("Texto 1 es mayor: {} que texto 2: {}".format(s, a))

elif s < a:
    print("Texto 2 es mayor: {} que texto 1: {}".format(a, s))


if texto_1[0]=="a" or texto_1[0]=="b" or texto_1[0]=="c" or texto_1[0]=="d" or texto_1[0]=="e" or texto_1[0]=="f" or texto_1[0]=="g" or texto_1[0]=="h" or texto_1[0]=="i" or texto_1[0]=="j" or texto_1[0]=="k" or texto_1[0]=="l" or texto_1[0]=="m" or texto_1[0]=="n" or texto_1[0]=="o" or texto_1[0]=="p" or texto_1[0]=="q" or texto_1[0]=="r" or texto_1[0]=="s" or texto_1[0]=="t" or texto_1[0]=="u" or texto_1[0]=="v" or texto_1[0]=="w" or texto_1[0]=="x" or texto_1[0]=="y" or texto_1[0]=="z":
    print("Texto 1: comienza con la letra {0}".format(texto_1[0]))


if texto_2[0]=="a" or texto_2[0]=="b" or texto_2[0]=="c" or texto_2[0]=="d" or texto_2[0]=="e" or texto_2[0]=="f" or texto_2[0]=="g" or texto_2[0]=="h" or texto_2[0]=="i" or texto_2[0]=="j" or texto_2[0]=="k" or texto_2[0]=="l" or texto_2[0]=="m" or texto_2[0]=="n" or texto_2[0]=="o" or texto_2[0]=="p" or texto_2[0]=="q" or texto_2[0]=="r" or texto_2[0]=="s" or texto_2[0]=="t" or texto_2[0]=="u" or texto_2[0]=="v" or texto_2[0]=="w" or texto_2[0]=="x" or texto_2[0]=="y" or texto_2[0]=="z":
    print("Texto 2: comienza con la letra {0}".format(texto_2[0]))


if texto_1[0] > texto_2[0]:
    print("Texto 1: {text1} es mayor que texto 2: {text2}".format(text1=texto_1, text2 = texto_2))
# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda


copia_texto_1 = texto_1  # Copia de la variable texto_1

if copia_texto_1 == texto_1:
    print(copia_texto_1, "es igual a texto_1" )

elif copia_texto_1 != texto_1:
    print(copia_texto_1," es diferente a ", texto_1)
# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda


# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
