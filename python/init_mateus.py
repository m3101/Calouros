class cachorro():
    def __init__(self,nome):
        self.nome = nome
    def latir(self):
        print(self.nome,"latiu")

bob = cachorro("bob")
bob.latir()