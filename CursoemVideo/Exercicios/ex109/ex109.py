import ex109Mod
preco = float(input('Digite um preço R$ '))
print(f'O dobro de {preco} é de {ex109Mod.dobro(preco, True)}')
print(f'A metade de {preco} é de {ex109Mod.metade(preco)}')
print(f'O aumento de 10% no valor é de {preco} é de {ex109Mod.aumentando(preco, 10)}')
print(f'O desconto de 10% no valor de {preco} é de {ex109Mod.diminuir(preco, 10)}')
