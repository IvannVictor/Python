import ex107Mod
preco = float(input('Digite um preço R$ '))
print(f'O dobro de R${preco} é de R${ex107Mod.dobro(preco)}')
print(f'A metade de R${preco} é de R${ex107Mod.metade(preco)}')
print(f'O aumento de 10% no valor é de R${preco} é de R${ex107Mod.aumentando(preco, 10)}')
print(f'O desconto de 10% no valor de R${preco} é de R${ex107Mod.diminuir(preco, 10)}')
