print('Progeção Aritimetica [PA]')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

termo = primeiro
c = 1
total = 0
mais = 11

while mais != 0:
    total = total + mais
    while c < total:
        print('{} -> '.format(termo), end='')
        c = c + 1
        termo = termo + razao
    print('Pausa')
    mais = int(input('\nQuer mais termos? Caso queira terminar, digite 0: '))
print('Programa finalizado com o total de {} termos'.format(c - 1))
