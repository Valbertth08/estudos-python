#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = ["a", "e", "i", "o", "u"]
consoante=[]
palavra = list(input("Informe a palavra: "))
count=0
if(len(palavra) <10):
    print("A palavra de conter 10 caracteres!")
else:
    for letra in palavra:
        if letra not in vogais:
            consoante.append(letra) 
            count+=1    
    print(f"consoantes: {consoante} quantidade: {count}")



    
