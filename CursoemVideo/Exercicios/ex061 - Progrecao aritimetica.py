print('Progeção aritimetica [PA]')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
c = 0

while c < 10:
    print('{} -> '.format(termo), end='')
    c = c + 1
    termo = termo + razao
print('Fim')
