from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Coprimento do cateto adiacentes: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
