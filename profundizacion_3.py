# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''




print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = int(input("1) Escribre la temperatura: "))
temperatura_2 = int(input("2) Escribre la temperatura: "))
temperatura_3 = int(input("3) Escribre la temperatura: "))


if temperatura_1 == temperatura_2:
    print("Temperaturas iguales")
    if temperatura_3 < temperatura_1 or temperatura_3 < temperatura_2:
        print("Temperatura 3 es menor")

if temperatura_1 > temperatura_2:
    print("Temperatura 1 es mayor que temperatura 2")
    if temperatura_3 < temperatura_1:
        print("Temperatura 3 es menor a temperatura 1")
    elif temperatura_3 < temperatura_2:
        print("Temperatura 3 es menor que temperatura 2")


if temperatura_2 > temperatura_1:
    print("Temperatura 2 es mayor que temperatura 1")
    if temperatura_3 < temperatura_2 or temperatura_3 < temperatura_1:
        print("Temperatura 3 es menor")

if temperatura_3 > temperatura_2 and temperatura_3 > temperatura_1:
    print("Temperatura 3 es mayor que temperatura 1 y 2")


promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3
print('El promedio es: ', promedio)