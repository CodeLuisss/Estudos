'''
programa que mostra o sucessor e antecessor de um número
'''

num = int(input('Insira um numero: '))

antecessor = num - 1
sucessor = num + 1

print(f'O antecessor de {num} é {antecessor} e o sucessor é {sucessor}.')

'''
Eu posso eliminar as duas variáveis "antecessor" e o "sucessor" e colocar dessa forma:
print(f'O antecessor de {num} é {num-1} e o sucessor é {num+1}.')
'''