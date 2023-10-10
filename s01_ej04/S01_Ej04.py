#complejidad de tiempo O(n)
#complejidad de espacio O(1)
numero = int(input("Ingrese su numero: "))

for i in range(11):
    print(str(numero) + " * " + str(i) + " = " + str(i*numero))

