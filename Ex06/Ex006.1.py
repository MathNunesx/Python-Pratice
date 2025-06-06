#SET

conjunto = {"Mega Drive", "Super Nintendo","Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
copia = conjunto.copy()
print(f"O conjunto original contém {conjunto}")
print(f"Ao gerar uma cópia utilizando o copy(), obtivemos {copia}")
copia.clear()
print(f"\nAo utilizar o método clear na cópia, ela ficou assim: \n{copia}")
print(f"Mas o conjunto original permanece inalterado: \n{conjunto}")
conjunto.pop()
print(f"\nAo utilizar o método pop() no conjunto, ele ficou assim: \n{conjunto}")
conjunto = {"Mega Drive", "Super Nintendo","Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"\nO conjunto foi recriado e agora contém \n{conjunto}")
conjunto.remove("Mega Drive")
print(f"Ao utilizar o método remove() com o item Mega Drive, o conjunto ficou assim \n{conjunto}, mas retornaria um erro caso o item não estivesse no conjunto")
conjunto = {"Mega Drive", "Super Nintendo","Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"\nO conjunto foi recriado e agora contém \n{conjunto}")
conjunto.discard("Mega Drive")
print(f"Ao utilizar o método discard() com o item Mega Drive o conjunto ficou assim \n{conjunto}, e não retornaria um erro caso o item não estivesse no conjunto")
