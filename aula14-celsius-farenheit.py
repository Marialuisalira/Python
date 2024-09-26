# 14-celsiu-farenheit.py = escreva um programa que converta uma temperatura
# digitada em °c em °f.
#  A fórmula para essa conversão é:
# f = (c * 9/5) + 32

celsius = float(input("Digite a temperatura em °C: "))
farenheit = 9 * celsius / 5 + 32
print(f"{celsius:.2f}°C é igual a {farenheit:.2f}°F")