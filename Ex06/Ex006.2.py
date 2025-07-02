# dicionario = {
# #     "name": "Star Wars - EP IV - A new Hope",
# #     "director": "George Lucas",
# #     "launch": 1977,
# #     "bilhetaria": 77500000.00
# # }
# #
# # print(f"O dicionario completo é {dicionario}")
# # print(f"O valor da chave do nome é {dicionario['nome']}")
# # dicionario["gênero"] = "Space Opera"
# # print(f"O dicionario completo é {dicionario}") errorrr"!!!!!!!!!!!!!!!
#


# Métodos keys | Values | Items
# dicionario = {
#     "name": "Star Wars - EP IV - A new Hope",
#     "director": "George Lucas",
#     "launch": 1977,
#     "bilhetaria": 77500000.00
# }


# print(f"O método .keys() retorna \n{dicionario.keys()}")
# print("Se percorrermos a lista retornada com um loop for teremos: ")
# for chave in dicionario.keys():
#     print(chave)
# print(f"\nO método .values() retorna \n{dicionario.values()}")
# print("Se percorrermos a lista retornada com um loop for teremos: ")
# for valor in dicionario.values():
#     print(valor)
# print(f"\nO método .items() retorna \n{dicionario.items()}")
# print("Como foi retornada uma lista de tuplas e as tuplas podem desempacotadas, teremos: ")
# for chave, valor in dicionario.items():
#     print(f"{chave} -- {valor}")

# Métodos Get | SetDefault | Copy

# dicionario = {
#     "name": "Star Wars - EP IV - A new Hope",
#     "director": "George Lucas",
#     "launch": 1977,
#     "bilhetaria": 77500000.00
# }
#
# print(f"O método .get() para a chave diretor retorna \n{dicionario.get('Director')}")
# print(f"O método .get() para a chave publico (que não existe) retorna \n{dicionario.get('publico')}")
# print(f"\n O método .setdefault() para a chave diretor retorna \n{dicionario.setdefault('director')}")
# dicionario.setdefault("publico")
# print(f" O método .setdefault() para a chave publico (que não existe) cria a chave e coloca o valor none como: \n{dicionario}")
# dicionario.setdefault("custo", 110000.0)
# print(f"Caso utilizemos o método .setdefault() a chave custo (q n existe) e tbm passarmos um Valor c/ argumetno, a key será criada com este valor:")
# print(f"\n O método .copy() retorna a seguinte copia do dicionario que, se for alterada, não impacta no dicionario original: {dicionario.copy()} ")

# Métodos update | pop | popitem | Clear

# dicionario = {
#     "nome": "Star Wars - Episódio IV - Uma nova esperança",
#     "diretor": "George Lucas",
#     "lançamento": 1977,
#     "bilheteria": 775000000.00
# }
# dicionario.update({"custo": 50.0})
# print(f"O método .update() com a chave custo (que não existia) e o valor 50.0 nos deixa com o seguinte dicionário \n{dicionario}")
# dicionario.update({"custo": 11000000.0})
# print(f"O método .update() com a chave custo (que já existe após a mudança anterior) e o valor 11000000.0 nos deixa com o seguinte dicionário \n{dicionario}")
# dicionario.pop("diretor")
# print(f"\nO método .pop() para a chave diretor nos deixa com o seguinte dicionário \n{dicionario}")
# dicionario.popitem()
# print(f"\nO método .popitem() nos deixa com o seguinte dicionário \n{dicionario}")
# dicionario.clear()
# print(f"\nO método .clear() nos deixa com o seguinte dicionário \n{dicionario}")

# Método fromKeys

# notas = dict.fromkeys(("Matemática", "Física", "Química"))
# print(f"O dicionário gerado com o método fromkeys para a tupla de chaves (Matemática, Física, Química) e sem valor foi: \n{notas}")
# notas = dict.fromkeys(("Matemática", "Física", "Química"), [])
# print(f"\nO dicionário gerado com o método fromkeys para a tupla de chaves (Matemática, Física, Química) e valor zero foi: \n{notas}")
