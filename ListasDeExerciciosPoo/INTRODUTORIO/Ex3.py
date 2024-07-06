#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
media=0;
nota=0;
count=0
notas=""
for numero in range(0,4):
    count+=1;
    nota=int(input(f"Informe a nota {count}: "))
    notas+=f"Nota {count}: {nota}"+"\n"
    media+=nota
print(notas)
print(f"A media final é: {media/4} ")