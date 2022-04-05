from time import sleep

print('\033[33m=-\033[m' * 30)
print('\033[36mContagem regresiva\033[m')
print('\033[33m=-\033[m' * 30)

for contagem in range(10, -1, -1):
   sleep(1)
   print(contagem)
print('Fooooogoooooooooo')
