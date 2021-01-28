class Pessoa:
    def __init__(self, nome=None, idade=47, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    alex = Pessoa(nome='Alex')
    itiro = Pessoa('Itiro', 47, alex)
    print(Pessoa.cumprimentar(itiro))
    print(id(itiro))
    print(itiro.cumprimentar())
    print(itiro.nome)
    for filho in itiro.filhos:
        print(filho.nome)
