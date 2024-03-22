nome=" jOaO"

print(nome.upper())#bota tudo maisculo
print(nome.lower())#bota tudo minusculo
print(nome.title())# coloca so o primeiro em maisculo


texto= " Ola mundo    "
print(texto.strip())# remove todos os espaços em branco
print(texto.lstrip())# remove todos os espaços em branco da esquerda
print(texto.rstrip())# remove todos os espaços em branco da direita

menu="Python"
print(menu.center(14,"#"))# centraliza a string e prenchendo de forma iguais com o caracter que foi definido
print(menu.center(14))# faz a mesma coisa, porem coloca o espaço em branco por  padrão(divide de forma iguais tbm)

print("-".join(menu))# itero no menu, e adiciono em cada item o .(ponto)

