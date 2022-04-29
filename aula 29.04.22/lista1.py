lista1 = [1,5,2]
lista2 = lista1[:] #copia a lista 1 - ##pode ser tbm lista2 = list(lista1)##
lista2[0] = 3
print(lista1)
print(lista2)
print(id(lista1))
print(id(lista2))

a = (1,2,3)
a[0] = 5