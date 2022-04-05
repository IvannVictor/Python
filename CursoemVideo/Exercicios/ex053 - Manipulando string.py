frase = str(input('Digite um frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
'''Modo simplificado "inverso = len(junto[::-1])"'''
for c in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]
print('O que e voce escreveu \033[32m"{}"\033[m escrita ao inverso fica "\033[33m{}\033[m"'.format(junto, inverso))

if inverso == junto:
    print('o que voce escreveu \033[36mela é palidromo\033[m')
else:
    print('Esse frase \033[31mnão\033[m é \033[31mpalidromo\033[m')
