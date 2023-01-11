m_n = input().split()
i = int(m_n[1])
lista = [int(x) for x in input().split()]

for index in range(len(lista)-i+1):
    soma = sum(lista[index:index+i])
    print(soma//i)