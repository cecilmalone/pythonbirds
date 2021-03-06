class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    cecil = Mutante(nome='Cécil')
    malone = Homem(cecil, nome='Malone')
    print(Pessoa.cumprimentar(malone))
    print(id(malone))
    print(malone.cumprimentar())
    print(malone.nome)
    print(malone.idade)
    for filho in malone.filhos:
        print(filho.nome)
    malone.sobrenome='Souza'
    del malone.filhos
    malone.olhos = 1
    del malone.olhos
    print(malone.__dict__)
    print(cecil.__dict__)
    print(Pessoa.olhos)
    print(malone.olhos)
    print(cecil.olhos)
    print(id(Pessoa.olhos), id(malone.olhos), id(cecil.olhos))
    print(Pessoa.metodo_estatico(), malone.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_class(), malone.nome_e_atributos_de_class())
    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(cecil, Pessoa))
    print(isinstance(cecil, Homem))
    print(cecil.olhos)
    print(malone.cumprimentar())
    print(cecil.cumprimentar())
