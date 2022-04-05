n1 = int(input('digite um valor: '))
print('Tabuada')
for ta in range(0, 10+1):
    re = n1 * ta
    print('''{} * {} = {}'''.format(n1, ta, re))
