calorias = []
resposta = ""

while resposta.upper() != "NÂO":
    caloria = int(input("Informe a quantidade de calorias nesta refeição:"))
    calorias.append(caloria)
    resposta = input("Digite SIM para informar mais uma caloria ou Não para encerrar a digitação: ")
total = 0
print("As calorias informadas foram: ")
for caloria in calorias:
    total = total + caloria
    print(caloria)
media = total /len(calorias)
print(f"Ao longo do dia foram consumidas {total} calorias, com uma média d {media:.2f} calorias por refeição!")