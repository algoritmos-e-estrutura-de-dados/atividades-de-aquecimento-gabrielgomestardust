nome = input()
salario = float(input())
ganhopessoal = float(input())

bonus = ganhopessoal*0.15 
total = salario + bonus

print("TOTAL = R$ %.2f" %total)