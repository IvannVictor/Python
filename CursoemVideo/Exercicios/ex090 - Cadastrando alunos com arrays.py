alunos = {}

alunos['Nome'] = str(input('Digite o nome do aluno: '))
nota = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
alunos['Media'] = (nota + nota2) / 2

if alunos['Media'] <= 5:
    alunos['Situação'] = 'Reprovado'
elif alunos['Media'] <= 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Aprovado'

print(f'O nome do aluno é {alunos["Nome"]}')
print(f'Sua media foi de {alunos["Media"]}')
print(f'Aluno {alunos["Nome"]}: {alunos["Situação"]}')
