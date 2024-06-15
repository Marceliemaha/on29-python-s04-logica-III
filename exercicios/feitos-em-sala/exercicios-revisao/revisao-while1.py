
numero = 1

while numero < 5: #enquanto o númeor for menor que 5 (< 5), execute o que está dentro do bloco interno.
    #bloco interno do while
    print(numero)
    numero = numero + 1 #roda a 1ª vez: entra no while, print(numero) que é 1. Soma 1 à variável numero (que é 1), resultando em 2; 
                        #roda a 2ª vez: entra no while, print(numero) que é 2. Soma 1 à variável numero (que agora é 2, porque subescrevemos a variável), resultando em 3; 
                        #roda a 3ª vez: entra no while, print(numero) que é 3. soma 1 à variável numero (que agora é 3, porque subescrevemos a variável), resultando em 4; 
                        #roda a 4ª vez: entra no while, print(numero) que é 4. Soma 1 à variável numero (que agora é 4, porque subescrevemos a variável), resultando em 5;
                        #roda a 5ª vez: não entra no while, porque a variável numero não é mais menor que 5 (< 5), agora ela é 5. Então, sai do bloco interno da função.
print("Fim de execução")#Printa 
