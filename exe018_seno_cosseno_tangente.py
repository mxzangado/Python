from math import radians, sin, cos, tan
ângulo = float(input('Digite o angulo que deseja: '))
seno = sin((radians(ângulo)))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ânulo de {} tem a Tangente de {:.2f}'.format(ângulo, tangente))