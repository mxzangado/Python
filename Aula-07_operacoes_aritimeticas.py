n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# \n contra barra siguinifica nova linha ou qubra de linha, end='' nao quebra linha.
print('A soma é {},\n o produuto é {}, é\n A Divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divião inteira {} e potencia {}'.format(di, e))
