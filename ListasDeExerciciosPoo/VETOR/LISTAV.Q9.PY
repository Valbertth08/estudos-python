#Utilize um vetor para receber a seguinte informação: Uma empresa paga seus vendedores com
#base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas
#brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma
#semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa
#(usando um array de contadores) que determine quantos vendedores receberam salários nos
#seguintes intervalos de valores:
#a. $200 - $299
#b. $300 - $399
#c. $400 - $499
#d. $500 - $599
#e. $600 - $699
#f. $700 - $799
#g. $800 - $899
#h. $900 - $999
#i. $1000 em diante
fun= ["a","b","c","d","e","f","g","h","i"]
vetor=[200,300,400,500,600,700,800,900,1000]
vbruta= [299,399,499,599,699,799,899,999,1000]
porc= []
soma=[]

for i in range(len(vbruta)):
    porc.append(vbruta[i]*(9/100))
for t in range (len(vetor)):
    soma.append(vetor[t]+porc[t])
for f in range (len(fun)):
    print(f'O funcionario {fun[f]}, recebeu o salario de {soma[f]:.2f} nesse mês')
