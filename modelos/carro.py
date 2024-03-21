class Carro:
    def __init__(self, modelo, cor, ano):    
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self) -> str:
        return f'{self.modelo} | {self.cor} | {self.ano}'
carro1 = Carro('500', 'branco', '2024')

print(carro1)