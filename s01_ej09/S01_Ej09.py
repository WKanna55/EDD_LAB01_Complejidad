# complejidad de tiempo O(n)
# complejidad de espacio O(1)
entrada = input("Ingrese palabra: ")

vocales = ['a', 'e', 'i', 'o', 'u'] #ov

suma = 0
for i in range(len(entrada)):
    print(entrada[i])
    for j in range(len(vocales)):
        if entrada[i] == vocales[j]:
            suma += 1

print(suma)