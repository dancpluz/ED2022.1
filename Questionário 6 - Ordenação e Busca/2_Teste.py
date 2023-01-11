n = int(input())
ordem = []

for _ in range(n):
    nome = input()
    parciais = [float(i) for i in input().split()]
    ordem += [(nome,sum(parciais))]

ordem.sort(key= lambda x: x[1])

for i in range(len(ordem)):
    if ordem[i][1]%60 < 10:
        print(f'{i+1}. {ordem[i][0]} ({int(ordem[i][1]/60)}:0{ordem[i][1]%60:.3f})')
    else:
        print(f'{i+1}. {ordem[i][0]} ({int(ordem[i][1]/60)}:{ordem[i][1]%60:.3f})')