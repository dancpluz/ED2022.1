class Queue:
    def __init__(self):
        self.items = []
        self.removidos = ''
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if self.items == []:
            return
        self.removidos += self.items[-1]
        return self.items.pop()

fila = Queue()
entrada = input()
saida = ''

for i in entrada:
    if i == '*':
        fila.dequeue()
    else:
        fila.enqueue(i)

print(fila.removidos)