class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    def dar_like(self):
        self.__likes += 1


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
print(f"Nome: {vingadores.nome}\tAno: {vingadores.ano}\tDuração: {vingadores.duracao}\tLikes:{vingadores.likes}")
print()
print(f"Nome: {atlanta.nome}\tAno: {atlanta.ano}\tTemporadas: {atlanta.temporadas}\tLikes:{atlanta.likes}")