class Pilha:
    def __init__(self):
        self.itens = []
        self.topo = None
        
    def push(self, obj):
        self.itens += [obj]
        print('Item adicionado à pilha.')
        self.topo = obj
                    
    def pop(self):
        if not self.isEmpty():
            print(f'Item {self.itens[-1]} removido da pilha.')
            self.itens.remove(self.itens[-1])
            if not self.isEmpty():
                self.topo = self.itens[-1]
            else:
                self.topo = None
                print('A pilha está vazia.')      
            
    def seek(self):
        if not self.isEmpty():
            print(f'Item do topo da pilha: {self.itens[-1]}.')
        else:
            print('A pilha está vazia.')
            
    def isEmpty(self):
        if not self.itens:
            return True
        return False
    
    
pilha1 = Pilha()

print('Adicione valores à pilha. Digite 0 para sair. \n')
while True:
    valor = int(input())
    
    if valor != 0:
        pilha1.push(valor)
    else:
        print('Encerrando...')
        break
    
pilha1.pop()
pilha1.isEmpty()
pilha1.seek()
