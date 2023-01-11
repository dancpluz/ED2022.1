class Stack:
    def __init__(self):
        self.pesos = []
        self.soma = 0
        self.contador = 0

    def push(self, item):
        self.pesos.insert(0,item)

    def pop(self):
        return self.pesos.pop(0)

    def isEmpty(self):
        return self.pesos == []

    def retirar(self):
        while not self.isEmpty():
            if self.pesos[0] == peso_desejado:
                self.soma += self.pesos[0]
                self.contador += 1
                print(f'Peso retirado: {self.pesos[0]}')
                print(f'Anilhas retiradas: {self.contador}')
                print(f'Peso total movimentado: {self.soma}')
                return
            else:
                print(f'Peso retirado: {self.pesos[0]}')
                self.soma += self.pesos[0]
                self.contador += 1
                self.pop()

    def retirar_tudo(self):
        for p in self.pesos:
            self.soma += p
            self.contador += 1
            print(f'Peso retirado: {p}')
        print(f'Anilhas retiradas: {self.contador}')
        print(f'Peso total movimentado: {self.soma}')

anilhas = Stack()
peso = int(input())

while peso != 0:
    anilhas.push(peso)
    peso = int(input())

peso_desejado = int(input())

if peso_desejado == 0:
    anilhas.retirar_tudo()
elif peso_desejado not in anilhas.pesos:
    anilhas.retirar_tudo()
else:
    anilhas.retirar()
