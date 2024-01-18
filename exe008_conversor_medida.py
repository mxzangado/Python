medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dec = medida * 10
deca = medida * 10
hec = medida * 100
km = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm '.format(medida, cm, mm))
print('Em {:.0f}dec e tambem coresponde a {:.0f}deca em {:.0f}hec e {:.0f}km '.format(dec, deca, hec, km))
