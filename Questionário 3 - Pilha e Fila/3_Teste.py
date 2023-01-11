class Queue:
    def __init__(self,com):
        self.items = []
        self.fator = int(com[1])
        self.peso = int(com[2])
        self.contador = 0
        self.tempo = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def verificar(self):
        self.contador -= 1
        if self.contador <= 0:
            self.contador = self.fator
            return True
        else:
            return False

    def fiscalizar(self):
        while not self.isEmpty():
            if self.verificar():
                if self.items[0] > self.peso:
                    primeiro = self.items[0]
                    self.tempo += 10
                    self.dequeue()
                    self.enqueue(primeiro - 2)
                else:
                    self.tempo += 5
                    self.dequeue()
            else:
                self.tempo += 1
                self.dequeue()
        return self.tempo

info = [int(i) for i in input().split()]
pesos = [int(i) for i in input().split()]
veiculos = Queue(info)

for p in pesos:
    veiculos.enqueue(p)

print(veiculos.fiscalizar())

