
n = input('Digite algo')

print('O tipo primitivo desse valor é:', type(n))

print('É um número?', n.isnumeric())

print('É alfabético?', n.isalpha())

print('É somente espaços?', n.isspace())

print('É minusculo?', n.islower())

print('É maiuscula?', n.isupper())

print('É alfanumérico?', n.isalnum())

print('Está capitalizada?', n.istitle())
