import random #funçao para gerar numeros aleatorios
import math

n1 = float(input("digite um numero "))
raiz = math.sqrt(n1)

print('A raiz do numero {}, é {:.2f}, a porção interia dele é {}'.format(n1, raiz, math.trunc(n1)))

n2 = random.randint(1, 10)
print(n2)

print('A porção inteira do numero é {}'.format(int(n1)))
