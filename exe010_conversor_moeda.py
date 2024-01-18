print('=' * 44)
print('------------CONVERSOR DE MOEDAS-------------')
real = float(input('Quanto Dinheiro você tem na carteira? R$ '))
dolar = real / 4.85
eur = real / 5.32
lib = real / 6.20
pesoargentino = real / 0.006

print('Com {:.2f} R$ você poderá comprar U$${:.2f}'.format(real, dolar))
print('Com {:.2f} R$ você pode comprar {:.2f} eur.'.format(real, eur))
print('Com {:.2f} R$ você pode comprar {:.2f} libras.'.format(real, lib))
print('Com {:.2f} R$ você pode comprar {:.2f} pesos argentinos'.format(real, pesoargentino))
print('=' * 44)
print('-------------------COVERSOR-----------------')
dolar = real * 4.85
eur = real * 5.32
lib = real * 6.20
pesoargentino = real * 0.006
print('Dolar U$$ {:.2f} terá valor em real de {:.2f}R$'.format(real, dolar))
print('Euro {:.2f} terá valor em real {:.2f}R$'.format(real, eur))
print('Libra {:.2f} terá valor em {:.2f}R$'.format(real, lib))
print('Pesos Argentinos {:.2f}pesos terá valor em {:.2f}R$'.format(real, pesoargentino))
print('=' * 44)