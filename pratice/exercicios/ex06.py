'''
programa conversor de dolar para real e real para dolar
'''        

money = float(input('Digite a quantidade de dinheiro que você tem: '))

dol = money * 0.20
real = money * 4.95

print(f'Se for BRL, você pode comprar apenas {dol:.2f} dólares!')
print(f'Se for Dolar, você pode comprar apenas {real:.2f} reais!')
