#Complejidad tiempo O(n)
#Complejidad espacio O(1)
numeroBuscar = int(input("Ingrese numero a buscar: "))

lista = [10,9,5,8,12,66,4]

for i in lista:
    print(i)
    if numeroBuscar == i:
        print("numero encontrado")
        break
