numero_tabuada = int(input('Informe o valor da tabuada: '))
comeco = int(input('Informe o começo da tabuada: '))
final = int(input('Informe o final da tabuada: '))

if final < comeco:
    final, comeco = comeco, final

for item in range(comeco, final+1, 1):
    print(f"{numero_tabuada}x {item}: {numero_tabuada*item}")

