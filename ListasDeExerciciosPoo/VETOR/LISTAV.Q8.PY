#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em
#um vetor. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas
#acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
#Fevereiro, . . . ). Utilize dois vetores um para cada informação.

from random import randint

soma=0
vetor=["janeiro","fevereiro","março","Abril","maio","junho","Julho","Agosto","Setembro","outubro","Novembro","Dezembro"]
tempm= [0]*12
for i in range(len(tempm)):
    tempm[i]= randint(0,43)
    soma+= tempm[i]
media= soma/12
for t in range(len(vetor)):
    if tempm[t]>media:
     print(f'A temeperatura acima da media é: {tempm[t]} e no mês ocorrido é {vetor[t]}')
print('As temperaturas são: ',tempm)
print('A media entre as temperaturas é: ',media)
#len só vai indicar o tamanho que vai ser percorrido e o t corresponde ao valores que são maiores
# que a temperatura estar acima da media
#um estar printando o valor e outro a posição 
    