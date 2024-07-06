#7- Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no
#seu respectivo vetor. Imprima a media das idades, a media das alturas, o mais novo, o mais velho,
#o mais alto e mais baixo.

from random import randint, uniform


idade= [0]*5
altura= [0]*5
soma= 0
media=0
menorid=0
maiorid=0
somal=0
medial=0
maioral=0
menoral=0


for i in range (len(idade)):
    idade[i]= randint(10,50)
    if i==0:
       menorid= idade[i]
       maiorid= idade[i]
    if idade[i] >maiorid:
        maiorid= idade[i]
    elif idade[i]<menorid:
        menorid= idade[i]
    soma+= idade[i]
    media= soma/5
print('As idades são',idade)   
print(' A soma entres as idades é: ',soma)
print('A media entre as idades é: ',media)
print('A mais velho é:',maiorid)
print('O mais novo é: ',menorid)
for t in range(len(altura)):
 altura[t]= uniform(1.40,2.0)
 if t==0:
    menoral= altura[t]
    maioral= altura[t]
 if altura[t]> maioral:
     maioral= altura[t]
 elif altura[t]< menoral:
     menoral= altura[t]
     soma+= altura[t]
     medial= soma/5
print('As alturas são: ',altura)
print('O mais alto é: ',maioral)
print('O mais baixo é: ',menoral)
print('A media da altura é: ',medial)





