# complejidad de tiempo O(n)
# complejidad de espacio O(1)
numero = int(input("ingrese un numero: "))

caracter = '$'
contador = 1
for i in range(numero):
    print(caracter * contador)
    contador += 1

