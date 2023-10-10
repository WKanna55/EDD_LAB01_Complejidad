#complejidad de tiempo O(n)
#complejidad de espacio O(1)
lista = [5,1,7,4,2,9,11]

max = -9999999999
for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]

print(max)
