#if aninhado 
conta_normal=False
conta_universitaria=True
saldo=2000
saque=2500
cheque_especial=50

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque<=(saldo+cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possivel realizar")
elif conta_universitaria:
    if saldo>=saque:
         print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
else:
    print("Sistema não reconheceu tipo de conta, entre em contato com sue gerente ")