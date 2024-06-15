lista_todos_valores = []

for numero in range(20):
    numero_validado = False
    while not numero_validado:
        try:
            lista_todos_valores.append(
                int(input(f'Informe um número {numero}: '))
            )
            numero_validado = True
        except:
            numero_validado = False


lista_impares = []
lista_pares = []

for item in lista_todos_valores:
    if item % 2: 
        lista_impares.append(item)
    else:
        lista_pares.append(item)

print(lista_pares)
print(lista_impares)
print(lista_todos_valores)
