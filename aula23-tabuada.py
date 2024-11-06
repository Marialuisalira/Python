#Solicita ao usuário que insira um número
numero = int(input("Digite um número para ver a sua tabuada: "))

#Exibe a tabuada do número
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")