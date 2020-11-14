class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def dar_like(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print()
print(f"{vingadores.nome} / {vingadores.ano} / {vingadores.duracao}min / {vingadores.likes} likes")
print(f"{atlanta.nome} / {atlanta.ano} / {atlanta.temporadas} temporadas / {atlanta.likes} likes")