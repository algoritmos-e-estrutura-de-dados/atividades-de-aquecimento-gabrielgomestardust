linha = input().split(' ')
linha1 = input().split(' ')

codeP, unidades, preco = linha
codeP1, unidades1, preco1 = linha1

total = (int(unidades) * float(preco)) + (int(unidades1) * float(preco1))

print('VALOR A PAGAR: R$ %.2f'%total)


