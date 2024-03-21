class Cliente:
    def __init__(self, nome, telefone, rg, idade):    
        self.nome = nome
        self.telefone = telefone
        self.rg = rg
        self.idade = idade

    def __str__(self) -> str:
        return f'{self.nome} | {self.telefone} | {self.idade} | {self.rg}'
    
cliente1 = Cliente('Jorge', '11111', '111111111111', '24')
cliente2 = Cliente('Maria', '222222', '222222222', '22')
cliente3 = Cliente('Pedro', '3333333', '33333333', '33')

print(cliente1, cliente2, cliente3)