#if

MAIOR_IDADE=18
IDADE_ESPECIAL=1718

idade=int(input("Informe sua idade"))

if idade >= 18:
    print("Maior de idade pode tirar a CNH")
if idade < MAIOR_IDADE:
    print("ainda não pode tirar CNH")

if idade >= 18:
    print("Maior de idade pode tirar a CNH")
else:
    print("ainda não pode tirar CNH")



if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas")
else:
    print("ainda não pode tirar CNH")