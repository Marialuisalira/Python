#Inicio da soma
soma = 0

#Loop para verificação dos números de 1 a 50
for numero in range(1, 51):
    #Verifica se o número é par
    if numero % 2 == 0:
        soma += numero  #Adiciona o número par à soma

#Exibir o resultado
print(f"A soma dos números pares entre 1 e 50 é: {soma}")
