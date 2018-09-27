class Pessoa:
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
