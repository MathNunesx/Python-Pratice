#Lista

#Adicionando
lista = [10, 9, 5]

lista.append("Teste de inserção")

print(lista)

print(lista[2])

#exibindo com Loop

for valor in lista:
    print(valor)


#remover
lista.pop()
print(lista)
lista.remove(9)
print(lista)

#tamanho da lista

print(len(lista))
