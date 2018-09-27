class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    cecil = Pessoa(nome='Cécil')
    malone = Pessoa(cecil, nome='Malone')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(malone.olhos)
    print(cecil.olhos)
    print(id(Pessoa.olhos), id(malone.olhos), id(cecil.olhos))
