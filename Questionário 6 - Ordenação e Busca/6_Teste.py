_ = input()
A = [int(i) for i in input().split()]
A_org = sorted(A,reverse=True)
B = []
k = 0
cont = 0

while A != A_org:
    mao = A[k]
    del A[k]
    while len(A) != k:
        if mao < A[k]:
            B.insert(0,mao)
            mao = A[k]
            A.pop(k)
        else:
            B.insert(0,A[k])
            A.pop(k)
    A += [mao]
    A += reversed(B)
    B = []
    k += 1

print(cont)