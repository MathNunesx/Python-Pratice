# TUPLA

enemy = [(10, 15), (30,30), (15,25), (7,10)]

for x, y in enemy:
    print(f"O inimigo está na posição X={x} e Y={y}")
x = int(input("Digite a posição X do inimigo que deseja acertar "))
y = int(input("Digite a posição y do inimigo que deseja acertar "))
if (x, y) in enemy:
    print(("Acertou!!!!!!"))
    enemy.remove((x,y))
else:
    print("Não foi encontrado nenhum inimigo na posição indicada ")
print(f"Os inimigos ainda existentes são: {enemy}")