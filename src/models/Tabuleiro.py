class Tabuleiro:

    def __init__(self):
        self.__total_casas = 64
        self.__livres = 64
        self.__ocupadas = [[]]
        self.__rainhas = []

    def __calcula_casas(self, posicao):
        coluna = posicao[1]
        linha = posicao[0]

        d_principal = 8 - abs(linha - coluna)
        d_secundaria = 8 - abs(linha + coluna - 9)

        #15 vem da horizontal + vertical(incluindo a casa atual)
        return (d_principal + d_secundaria - 2) + 15 
    
    def __posicoes(self, posicao):
        linha = posicao[0]
        coluna = posicao[1]

        casas = [(linha, j) for j in (8)]
        casas += [(i, coluna) for i in (8)]

    def add_rainha(self, posicao):
        casas = self.__calcula_casas(posicao)