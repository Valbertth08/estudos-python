#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual 

count=0
count2=0
soma=0
medias=[]
for i in range (0,3):
    count+=1
    for f in range(0,4):
        count2+=1
        nota=int(input(f"Informe a {count2} nota do aluno({count}): ")) 
        soma+=nota
    medias.append(soma/4)
    count2=0
    soma=0
alunos=0
for nota in medias:
    if(nota >=7):
        alunos+=1
print("Media de todos os alunos: ",medias)
print("Alunos com meida maior ou igual a 7: ",alunos)