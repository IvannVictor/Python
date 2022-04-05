import ex108Mod
preco = float(input('Digite um preço R$ '))
print(f'O dobro de {ex108Mod.formatação(preco)} é de {ex108Mod.formatação(ex108Mod.dobro(preco))}')
print(f'A metade de {ex108Mod.formatação(preco)} é de {ex108Mod.formatação(ex108Mod.metade(preco))}')
print(f'O aumento de 10% no valor é de {ex108Mod.formatação(preco)} é de {ex108Mod.formatação(ex108Mod.aumentando(preco, 10))}')
print(f'O desconto de 10% no valor de {ex108Mod.formatação(preco)} é de {ex108Mod.formatação(ex108Mod.diminuir(preco, 10))}')
