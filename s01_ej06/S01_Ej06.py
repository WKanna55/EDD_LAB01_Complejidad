#complejidad tiempo O(n)
#Complejidad O(n)
lista = []

pares = []
impares = []

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
