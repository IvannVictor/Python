import urllib
import urllib.request

try:
    site = urllib.request.urlopen(input('Digite a URL que deseja testar (Por favor digite tudo http...): '))
except:
    print('Site indisponivel [Erro de internet ou site mudado para outra URL')
else:
    print('Site perfeitamente no ar')
    # print(site.read()) Podemos usar para ler o HTML do site