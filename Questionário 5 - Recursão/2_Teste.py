def printMover(de,para):
    print(f'Mover de {de} para {para}.')

def Mover(de,para,temp,altura):
    if altura >= 1:
        Mover(de, temp, para, altura-1)
        printMover(de, para)
        Mover(temp, para, de, altura-1)

entrada = input().split()
Mover(entrada[1],entrada[2],entrada[3],int(entrada[0]))