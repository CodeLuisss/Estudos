'''
Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))

A = l * h
litros = A / 2

print(f'A parede tem uma Área de {A} metros quadrados e são necessários {litros} litros de tinta para pintar essa parede!')