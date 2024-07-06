f = 5
idade = [1]*f
alt = [1]*f
m_novo = 0
m_velho = 0
m_alto = 0
m_baixo = 0

for i in range (len(idade)):
    idade[i]= int(input("Digite a idade: ")) 
    if i == 0:
        m_novo = idade[i] 
        m_velho = idade[i]
    elif idade [i] < m_novo:
        m_novo = idade [i]
    elif idade [i] > m_velho:
        m_velho = idade [i]
for t in range (len(alt)):
    alt[t]= float(input("Digite a altura: ")) 
    if t == 0:
        m_alto = alt[t]
        m_baixo = alt[t]
    elif alt [t] > m_alto:
        m_alto = alt [t]
    elif alt[t] < m_baixo:
        m_baixo = alt[t] 
print("A menor idade: ",m_novo)
print("A maior idade é: ",m_velho)
print("O mais alto é: ",m_alto)
print("O mais baixo é: ",m_baixo)
print(f"A  média de altura é:{sum(alt)/f:.2f}")
print(f"A  média de idade é:{sum(idade)/f}")