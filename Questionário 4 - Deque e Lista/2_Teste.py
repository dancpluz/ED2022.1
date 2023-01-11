class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def checkComando(lista):
    comando = lista[0]

    if comando == 'P':
        print(deque.removeFront())
    elif comando == 'D':
        print(deque.removeRear())
    else:
        valor = lista[1]
        if comando == 'I':
            deque.addRear(valor)
        else:
            deque.addFront(valor)

entrada = input()
deque = Deque()

while entrada != 'X':
    checkComando(entrada.split())
    entrada = input()

for i in deque.items:
    print(i)
