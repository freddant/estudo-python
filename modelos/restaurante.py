class Restaurante:
    restaurantes = []

    '''
    Init: um construct (funçao) que é chamado sempre que uma 
    classe é instanciada, com ele é possivel criar pré-requisitos
    para a criação de um objeto da nossa classe.
    O python possuí varios metodos padrão para classes
    Init é um deles
    print(dir(objeto da classe)) mostra todos os metodos
    que a classe possui
    '''
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        '''
        Aqui usamos o metodo str, outro metodo padrão
        Quando fazemos print(objeto da classe) temos como retorno
        o endereço do espaço de memória.
        Usando o método str podemos setar o que vai exibido
        quando printarmos a classe em formato de texto
        '''
        return f'{self.nome}' | {self.categoria}

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Planet', 'Italiana')

Restaurante.listar_restaurantes()
#print(vars(restaurante_pizza))
#print(dir(restaurante_praca))

# restaurante_praca.nome = 'Bistrô'
# restaurante_praca.categoria = 'Italiana'

# print(restaurante_praca.nome)
# #print(dir(restaurante_praca))
# if restaurante_praca.ativo:
#     print('Restaurante aberto')
# else:
#     print('Restaurante fechado')
# print(restaurante_praca.ativo)
# dir(objeto da classe) vai exibir os metodos da classe, útil para classes desconhecidas
# vars(objeto da classe) vai exibir os atributos 

# restaurante_pizza = Restaurante()
# restaurante_pizza.nome = 'Pizza Planet'
# restaurante_pizza.categoria = 'Fast Food'
# restaurante_pizza.ativo = True

# print(restaurante_praca.nome, restaurante_praca.categoria)
