lista_de_todos_valores = []

for numero in range(20):
    lista_de_todos_valores.append(numero)

lista_impares = []
lista_pares = []

for item in lista_de_todos_valores:
    if item % 2: 
        lista_impares.append(item)
    else:
        lista_pares.append(item)

print(lista_pares)
print(lista_impares)
print(lista_de_todos_valores)

