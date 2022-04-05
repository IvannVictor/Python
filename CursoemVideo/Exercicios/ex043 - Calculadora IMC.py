from time import sleep

print('\033[33m=-\033[m' * 30)
print('\033[36mVamos calcular seu indece de massa corporal(IMC)\033[m')
print('\033[33m=-\033[m' * 30)

peso = float(input('Digite seu peso, \033[31msem mentir!:\033[m '))
altura = float(input('Digite a sua altura: '))
altura = altura * altura
imc = peso / altura

sleep(2)
print('\033[1:31:43mEstamos calculando para voce .....\033[m')

sleep(2)
if imc < 18.5:
    print('Seu peso esta \033[31mabaixo do ideal!! Alimente-se melhor!!\033[m')
elif imc < 25:
    print('Seu peso é o \033[32mideal!! Mantenha-se assim!!\033[m')
elif imc < 30:
    print('Voce esta com \033[33msobrepeso!! Cuide um pouco melhor da sua alimentação!!\033[m')
elif imc < 40:
    print('Voce esta \033[34macima\033[m do peso!! \033[35mCuide-se melhor, e faça exercicios!!\033[m')
else:
    print('Voce esta com \033[35mobsidade morbida!! Pocure um medico nutricionista para ajudar voce!!\033[m')
