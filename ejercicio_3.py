# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados
numero_1 = 6
numero_2 = -3

if numero_1 > 5:
    print("Numero 1 es mayor a 5")
    if numero_2 < 0:
        print("Resp=1")
    elif numero_2 >= 0:
        print("Resp=2")

if numero_1 < 5:
    print("Numero 1 es menor a 5")
    if numero_2 > 5:
        print("Resp=3")
    elif numero_2 < 5:
        print("Resp=4")

# Verifique si el numero_1 es mayor a 5
#   --> En caso afirmativo, verifique si el numero_2
#       es positivo
#       --> En caso afirmativo imprima en pantalla "Resp=1"
#       --> En caso negativo imprima en pantalla   "Resp=2"
#  --> En caso negativo (numero_1 no es mayor a 5)
#      verifique si el numero_2 es mayor a 5
#       --> En caso afirmativo imprima en pantalla "Resp=3"
#       --> En caso negativo imprima en pantalla "Resp=4"

# Verifique la calificación de un estudiante según su
# puntaje en un examen
puntaje = 90

if puntaje >= 90:
    print("A")
elif puntaje >= 80:
    print("B")
elif puntaje >= 70:
    print("C")
elif puntaje >= 60:
    print("D")
elif puntaje < 60:
    print("F")


# Si el puntaje es mayor igual a 90 --> imprimir A
# Si el puntaje es mayor igual a 80 --> imprimir B
# Si el puntaje es mayor igual a 70 --> imprimir C
# Si el puntaje es mayor igual a 60 --> imprimir D
# Si el puntaje es menor a  60      --> imprimir F

# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados