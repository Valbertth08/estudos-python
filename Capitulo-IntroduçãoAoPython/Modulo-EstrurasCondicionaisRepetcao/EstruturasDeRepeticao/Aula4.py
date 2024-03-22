
while True:# gerando um lopp infinito
    opcao=int(input("Informe um numero "))
    if opcao == 10:
        break# ele interrompe a execução do loop por determinado condição 
    print(opcao)


for numero in range(15):
    if(numero == 10):# quebrando a execução do loop
        break

    print(numero)


for numero in range(15):
    if(numero == 10):# quebrando a execução do loop
        continue # serve para pular alguma execucação de um numero, caso ele satisfaça alguma condição 
        #Esse eu não executo quando o valor for 10(ou seja, ele pula a exeucação)

    print(numero)