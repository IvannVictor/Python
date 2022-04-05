from datetime import datetime

tra = dict()

tra["Nome"] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimeto: '))
tra["Idade"] = datetime.now().year - nascimento
tra["Car"] = int(input('Nº da carteira de trabalho (0 p/ caso não tenha): '))
if tra["Car"] != 0:
    tra["AnoC"] = int(input('Ano de contratação: '))
    tra["Salario"] = float(input('digite o seu salario: '))
    # soma o ano mais 35 e subitrai a idade ficando assim o ano que ele ira se aposentar
    tra["aposentadoria"] = tra["Idade"] + ((tra["AnoC"] + 35) - datetime.now().year)

print()
print('-=' * 30)

for i, t in tra.items():
    print(f'{i} = {t}')
