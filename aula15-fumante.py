# Escreva um progama para calcular a redução do tempo de vida de um fumante
# Pergunte a quantidade de cigarros fumados por dia e quantos ele já 
# fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
# e calcule quantos dias de vida de um fumante perderá. Exiba o total em dias.

cigarros_por_dia = int(input("Quantidade de cigarros por dia:"))
anos_fumando = float(input("Quantidade de anos fumando:"))
redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
# Um dia tem 24 x 60 minutos
redução_em_dias = redução_em_minutos / (24 * 60)
print(f"Redução do tempo de vida {redução_em_dias:.2f} dias")