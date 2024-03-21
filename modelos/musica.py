class Musica:
    def __init__(self, artista, duracao, nome):    
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

m1 = Musica('Los Sebosos Postizos', 2.26, 'Quero Esquecer Você')
m1.artista = 'Los Sebosos Postizos'
m1.duracao = 2.26
m1.nome = 'Quero Esquecer Você'

m2 = Musica('Jorge Ben Jor', 3.48, 'O Telefone Tocou Novamente')
m2.artista = 'Jorge Ben Jor'
m2.duracao = 3.48
m2.nome = 'O Telefone Tocou Novamente'

m3 = Musica('Gilsons', 2.36, 'Vento Alecrim')
m3.artista = 'Gilsons'
m3.duracao = 2.36
m3.nome = 'Vento Alecrim'

print(m1)