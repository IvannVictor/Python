from builtins import print
from time import sleep

print('\033[32m=-'*30)
print('\033[7:34mConversor de numeros\033[m')
print('\033[32m=-\033[m'*30)

valor = int(input('Digite o numero que queira converter: '))

print('''Escolha a conversão de acordo com 0 codigo dela
\033[33m[ 1 ]\033[m Converter para \033[33mBINARIO\033[m
\033[33m[ 2 ]\033[m Converter para \033[33mOCTAL\033[m
\033[33m[ 3 ]\033[m Converter para \033[33mHEXADECIMAL\033[m''')

conver = int(input('Digite o codigo da conversão: '))

sleep(2)

if conver == 1:
    print('O codigo escolhido foi \033[31m1 BINARIO\033[m')
elif conver == 2:
    print('O codigo escolhido foi \033[31m2 OCTAL\033[m')
elif conver == 3:
    print('O codigo escolhido foi \033[31m3 HEXADECIMAL\033[m')
else:
    print('\033[32mCodigo não localizado\033[m')

sleep(2)
print('\033[35mConvertendo.....\033[m')

sleep(2)
if conver == 1:
    print('O numero \033[36m{}\033[m, convertido para BINARIO é \033[37m{}\033[m'.format(valor, bin(valor)[2:]))
elif conver == 2:
    print('O numero \033[36m{}\033[m, convertido para OCTAl é \033[37m{}\033[m'.format(valor, oct(valor)[2:]))
elif conver == 3:
    print('O numero \033[36m{}\033[m, convertido para HEXADECIMAL é \033[37m{}\033[m'.format(valor, hex(valor)[2:]))
else:
    print('\033[31mPor favor digite um codigo valido\033[m')
